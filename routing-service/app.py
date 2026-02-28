import openrouteservice
import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

ors = openrouteservice.Client(
    key=os.getenv("ORS_API_KEY")
)

def get_place_name(lon, lat):
    try:
        result = ors.reverse_geocode([lon, lat])
        return result["features"][0]["properties"]["label"]
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
