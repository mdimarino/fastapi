#!/usr/bin/env python

import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Star Trek Ships', 
              description='System to manage Star Trek Ships', 
              version='0.0.1', 
              contact={'Author':'Marcello Di Marino Azevedo', 'E-mail': 'marcello@di.marino.nom.br'})

class Ship(BaseModel):
    Name: str
    Class: str
    Owner: str
    Operator: str
    Status: str

ships = {
    'NCC-1701-E': Ship(Name = 'USS Enterprise', Class = 'Sovereign-class',     Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NX-74205':   Ship(Name = 'USS Defiant',    Class = 'Defiant-class',       Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Destroyed'),
    'NCC-74656':  Ship(Name = 'USS Voyager',    Class = 'Intrepid-class',      Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NCC-1031-A': Ship(Name = 'USS Discovery',  Class = 'Crossfield-class',    Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NCC-75567':  Ship(Name = 'USS Cerritos',   Class = 'California-class',    Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NCC-58925':  Ship(Name = 'USS Pasteur',    Class = 'Olympic-class',       Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Destroyed'),
    'NCC-65420':  Ship(Name = 'USS Phoenix',    Class = 'Nebula-class',        Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NCC-72381':  Ship(Name = 'USS Equinox',    Class = 'Nova-class',          Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Destroyed'),
    'NCC-14598':  Ship(Name = 'USS Fearless',   Class = 'Excelsior-class',     Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NCC-2893':   Ship(Name = 'USS Stargazer',  Class = 'Constellation-class', Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Recovered'),
    'NCC-317856': Ship(Name = 'USS Armstrong',  Class = 'Armstrong-type',      Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NCC-1227':   Ship(Name = 'USS Shenzhou',   Class = 'Walker-class',        Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Abandoned'),
    'NX-74913':   Ship(Name = 'USS Prometheus', Class = 'Prometheus-class',    Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NCC-80102':  Ship(Name = 'USS Titan',      Class = 'Luna-class',          Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Active'),
    'NCC-1648':   Ship(Name = 'USS Europa',     Class = 'Nimitz-class',        Owner = 'United Federation of Planets', Operator = 'Starfleet', Status = 'Destroyed')
}

# ships = {}

@app.get("/ships")
async def get_ships():
    
    """Return all ships"""
    
    if len(ships) != 0:
        return ships
    return None

@app.get("/ship/{ship_registry}")
async def get_ship(ship_registry: str):

    """Return a ship, if it exists"""

    if ship_registry in ships.keys():
        return {ship_registry: ships[ship_registry]}
    return None

@app.post("/ship/{ship_registry}")
async def create_ship(ship_registry: str, new_ship: Ship):

    """Add a ship, if it not exists"""

    if ship_registry not in ships.keys():
        ships[ship_registry] = new_ship
        return {ship_registry: ships[ship_registry]}
    return None

@app.put("/ship/{ship_registry}")
async def change_ship(ship_registry: str, changed_ship: Ship):

    """Change a ship, if it exists"""

    if ship_registry in ships.keys():
        ships[ship_registry] = changed_ship
        return {ship_registry: ships[ship_registry]}
    return None

@app.delete("/ship/{ship_registry}")
async def delete_ship(ship_registry: str):

    """Delete a ship, if it exists"""

    if ship_registry in ships.keys():
        return {ship_registry: ships.pop(ship_registry)}
    return None

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug", reload=True)
