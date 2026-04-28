
# Equipo 4


# PumaRide
An open source project made by and for college students of ENES Morelia in 
mind that aims 
to give them a platform where they can request free rides depending on 
where they are and where they want to go within the community members of 
UNAM Morelia
 -development-

## Collaborators:

* Technology Engineer: Adrián Lara Álvarez
* Testing Engineer: Emiliano Ramírez.
* Project Manager: Grecia Leilani Arias Avalos

## Software
This project relies completely on the openrouteservice API. It provides the necessary tools to calculate the most
effective routes in the map.
All of the coordinates and location names are extracted from the [following map](https://maps.openrouteservice.org/#/),
associated to openrouteservice itself.
We are using FastAPI for the structure itself, and we manage data requests using HTTP.

## Usage of app.py in routing-service in a development enviroment
To use this test script and obtain information from the openrouteservice API,
you first need to install the necessary dependencies (FastAPI, uvicorn, python-dotenv, openrouteservice)

After that, you need access to your own API key which you will use to communicate
with the openrouteservice server. You can get it for free by logging in their site
and opening the API playground. Using your API key, you will modify your .env file
and the script should work properly.

In your terminal and in the directory pumaride/routing-service, run:

```python
uvicorn app:app --reload
```

Then in your browser use the link that shows up on the terminal followed by /docs
to open the Swagger UI.

In this interface, you can try out the API using the correct format. Entering two
coordinates in [lon, lat]. It should return a .JSON file with the names of both
the start point and the end point, followed by the distance in km and the 
estimated duration of the trip in minutes. You might want to use these for ease of use:

* start: -101.230103,19.647981
* end: -101.217813,19.679336

<details>
  <summary>Click to view code</summary>
 
  ```python
  import openrouteservice
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI()

ors = openrouteservice.Client(
    key=os.getenv("ORS_API_KEY")
)

def get_place_name(lon, lat):
    try:
        result = ors.pelias_reverse(
            point=[lon, lat]
        )

        features = result.get("features", [])

        if not features:
            return "Unknown location"

        return features[0]["properties"].get("label", "Unknown location")

    except Exception as e:
        print("Reverse geocode error:", e)
        return "Unknown location"

@app.get("/route")
def get_route(start: str, end: str):
    start_coords = start.split(",")
    end_coords = end.split(",")

    coords = [
        [float(start_coords[0]), float(start_coords[1])],
        [float(end_coords[0]), float(end_coords[1])]
    ]

    route = ors.directions(coords)

    if "routes" not in route:
        return {"error": "Route not found", "response": route}

    summary = route["routes"][0]["summary"]

    start_name = get_place_name(coords[0][0], coords[0][1])
    end_name = get_place_name(coords[1][0], coords[1][1])

    return {
        "start_name": start_name,
        "end_name": end_name,
        "distance_km": round(summary["distance"] / 1000, 2),
        "duration_min": round(summary["duration"] / 60, 2)
    }
 ```
