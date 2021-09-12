#!/usr/bin/env python

import requests, json

BASE = "http://192.168.99.140:31640/"

data = [
    {"Name": "USS Enterprise", "Class": "Sovereign-class",     "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Defiant",    "Class": "Defiant-class",       "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Voyager",    "Class": "Intrepid-class",      "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Discovery",  "Class": "Crossfield-class",    "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Cerritos",   "Class": "California-class",    "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Pasteur",    "Class": "Olympic-class",       "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Destroyed"},
    {"Name": "USS Phoenix",    "Class": "Nebula-class",        "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Equinox",    "Class": "Nova-class",          "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Destroyed"},
    {"Name": "USS Fearless",   "Class": "Excelsior-class",     "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Stargazer",  "Class": "Constellation-class", "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Recovered"},
    {"Name": "USS Armstrong",  "Class": "Armstrong-type",      "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Shenzhou",   "Class": "Walker-class",        "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Abandoned"},
    {"Name": "USS Prometheus", "Class": "Prometheus-class",    "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Titan",      "Class": "Luna-class",          "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Active"},
    {"Name": "USS Europa",     "Class": "Nimitz-class",        "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Destroyed"}

]

print("=== Inserting ships ==")

response = requests.post(BASE + "ship/" + "NCC-1701-E", json=data[0])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NX-74205", json=data[1])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-74656", json=data[2])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-1031-A", json=data[3])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-75567", json=data[4])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-58925", json=data[5])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-65420", json=data[6])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-72381", json=data[7])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-14598", json=data[8])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-2893", json=data[9])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-317856", json=data[10])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-1227", json=data[11])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NX-74913", json=data[12])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-80102", json=data[13])
print(json.dumps(response.json(), indent=2))

response = requests.post(BASE + "ship/" + "NCC-1648", json=data[14])
print(json.dumps(response.json(), indent=2))

print("=== Updating ships ==")

data[1] = {"Name": "USS Defiant", "Class": "Defiant-class", "Owner": "United Federation of Planets", "Operator": "Starfleet", "Status": "Destroyed"}

response = requests.put(BASE + "ship/" + "NX-74205", json=data[1])
print(json.dumps(response.json(), indent=2))

print("=== Deleting ships ===")

response = requests.delete(BASE + "ship/" + "NX-74205")
print(json.dumps(response.json(), indent=2))

print("=== Recovering a ship ===")

response = requests.get(BASE + "ship/" + "NCC-74656")
print(json.dumps(response.json(), indent=2))

print("=== Recovering all ships ===")

response = requests.get(BASE + "ships")
print(json.dumps(response.json(), indent=2))
