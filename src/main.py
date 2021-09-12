#!/usr/bin/env python

import uvicorn
import redis
import json

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseSettings, BaseModel, Field


class Settings(BaseSettings):
    uvicorn_host: str
    uvicorn_port: int
    uvicorn_log_level: str
    uvicorn_workers: int
    uvicorn_reload: bool
    redis_host: str
    redis_port: int
    redis_database: int
    redis_decode_responses: bool

    class Config:
        env_file = ".envvars"


class Ship(BaseModel):
    Name: str = Field(..., example = "USS Titan")
    Class: str = Field(..., example = "Luna-class")
    Owner: str = Field(..., example = "United Federation of Planets")
    Operator: str = Field(..., example = "Starfleet")
    Status: str = Field(..., example = "Active")

    class Config:
        schema_extra = {
            "example": {
                "Name": "USS Titan",
                "Class": "Luna-class",
                "Owner": "United Federation of Planets",
                "Operator": "Starfleet",
                "Status": "Active",
            }
        }

settings = Settings()

app = FastAPI(title='Star Trek Ships', 
              description='System to manage Star Trek Ships', 
              version='0.0.1', 
              contact={'Author':'Marcello Di Marino Azevedo', 
                       'E-mail': 'marcello@di.marino.nom.br'})


r = redis.Redis(host=settings.redis_host,
                port=settings.redis_port,
                db=settings.redis_database,
                decode_responses=settings.redis_decode_responses)

@app.get(path = "/")
async def root():

    """Handles Root Calls"""

    return {"message": "nothing to see here move along..."}

@app.get("/ships", status_code=status.HTTP_200_OK)
async def get_ships():

    """Return all ships"""

    try:
        if len(r.keys()) != 0:
            ships = {}
            for key in r.keys():
                ships[key] = json.loads(r.get(key))
            return ships
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection failure to Redis")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")

@app.get("/ship/{ship_registry}", status_code=status.HTTP_200_OK)
async def get_ship(ship_registry: str):

    """Return a ship, if it exists"""

    try:
        if r.exists(ship_registry):
            ship = json.loads(r.get(ship_registry))
            return {ship_registry: ship}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection failure to Redis")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.post("/ship/{ship_registry}", status_code=status.HTTP_201_CREATED)
async def create_ship(ship_registry: str, new_ship: Ship):

    """Add a ship, if it not exists"""

    try:
        if not r.exists(ship_registry):
            r.set(ship_registry, new_ship.json())
            return {ship_registry: new_ship}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection failure to Redis")
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Item already exists")

@app.put("/ship/{ship_registry}", status_code=status.HTTP_202_ACCEPTED)
async def change_ship(ship_registry: str, changed_ship: Ship):

    """Change a ship, if it exists"""

    try:
        if r.exists(ship_registry):
            r.set(ship_registry, changed_ship.json())
            return {ship_registry: changed_ship}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection failure to Redis")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.delete("/ship/{ship_registry}", status_code=status.HTTP_200_OK)
async def delete_ship(ship_registry: str):

    """Delete a ship, if it exists"""

    try:
        if r.exists(ship_registry):
            deleted_ship = json.loads(r.get(ship_registry))
            r.delete(ship_registry)
            return {ship_registry: deleted_ship}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection failure to Redis")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run("main:app", 
                 host = settings.uvicorn_host, 
                 port = settings.uvicorn_port, 
                 log_level = settings.uvicorn_log_level, 
                 workers = settings.uvicorn_workers, 
                 reload = settings.uvicorn_reload)
