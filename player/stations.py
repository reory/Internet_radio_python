# Radio station file to update radio station information from a json file.

import json
import os

def load_stations():
    """Load station list from stations.json"""
    json_path = os.path.join(os.path.dirname(__file__), "stations.json")

    with open(json_path, "r", encoding="utf-8") as f:
        data =  json.load(f)
    
    stations = {}

    for country_code, station_block in data.items():
        if country_code.startswith("_"):
            continue # skip comments

        for name, info in station_block.items():
            stations[name] = {
                "url": info["url"],
                "category": info.get("category", "Unknown"),
                "country": country_code
            }
            
    return stations

