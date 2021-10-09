#!/usr/bin/env python

import uvicorn
import redis
import json

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseSettings, BaseModel, Field
from pyfiglet import Figlet


class Ship(BaseModel):
    Name: str = Field(..., example="USS Titan")
    Class: str = Field(..., example="Luna-class")
    Owner: str = Field(..., example="United Federation of Planets")
    Operator: str = Field(..., example="Starfleet")
    Status: str = Field(..., example="Active")

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


class Settings(BaseSettings):
    app_title: str
    app_description: str
    app_version: str
    app_contact_author: str
    app_contact_email: str
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

settings = Settings()

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
    contact={
        "Author": settings.app_contact_author,
        "E-mail": settings.app_contact_email
    }
)

r = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_database,
    decode_responses=settings.redis_decode_responses
)


@app.on_event("startup")
async def startup_event():
    custom_fig = Figlet(font="banner3")
    print(custom_fig.renderText(settings.app_title))


@app.on_event("shutdown")
async def shutdown_event():
    custom_fig = Figlet(font="banner3")
    print(custom_fig.renderText("shutdown"))


@app.get("/")
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
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ship not found")


@app.get("/ship/{ship_registry}", status_code=status.HTTP_200_OK)
async def get_ship(ship_registry: str):

    """Return a ship, if it exists"""

    try:
        if r.exists(ship_registry):
            ship = json.loads(r.get(ship_registry))
            return {ship_registry: ship}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection failure to Redis")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ship not found")


@app.post("/ship/{ship_registry}", status_code=status.HTTP_201_CREATED)
async def create_ship(ship_registry: str, new_ship: Ship):

    """Add a ship, if it not exists"""

    try:
        if not r.exists(ship_registry):
            r.set(ship_registry, new_ship.json())
            return {ship_registry: new_ship}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection failure to Redis")
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Ship already exists")


@app.put("/ship/{ship_registry}", status_code=status.HTTP_202_ACCEPTED)
async def change_ship(ship_registry: str, changed_ship: Ship):

    """Change a ship, if it exists"""

    try:
        if r.exists(ship_registry):
            r.set(ship_registry, changed_ship.json())
            return {ship_registry: changed_ship}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Connection failure to Redis")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ship not found")


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
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ship not found")


if __name__ == "__main__":

    log_config = uvicorn.config.LOGGING_CONFIG

    log_config["formatters"]["default"]["fmt"] = "[%(asctime)s] %(levelprefix)s %(message)s"
    log_config["formatters"]["access"]["fmt"] = "[%(asctime)s] %(levelprefix)s %(client_addr)s - \"%(request_line)s\" %(status_code)s"

    uvicorn.run(
        "main:app", 
        host=settings.uvicorn_host,
        port=settings.uvicorn_port,
        log_level=settings.uvicorn_log_level,
        workers=settings.uvicorn_workers,
        reload=settings.uvicorn_reload,
        log_config=log_config
    )
