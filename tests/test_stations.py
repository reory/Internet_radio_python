import json
import builtins
from unittest.mock import mock_open, patch
from player.stations import load_stations

def test_load_station_basic():
    """Mock JSON structure similar to real file"""

    mock_json = json.dumps({
        "US": {
            "ROCK FM": {"url": "http://rock.fm/stream", "category": "ROCK"},
            "JAZZ FM": {"url": "http://jazz.fm/stream"} # unknown category.
        },
        "_comment": {
            "IgnoreMe": {"url": "http://ignore.me"}
        },
        "UK": {
            "BBC RADIO 1": {"url": "http://bbc.co.uk/stream", "category": "POP"}
        }
    })

    # Patch open() so load_stations reads our fake JSON 
    # instead of the real files.
    with patch.object(builtins, "open", mock_open(read_data=mock_json)):
        stations = load_stations()

    # Ensure all expected stations are present.
    assert "ROCK FM" in stations
    assert "JAZZ FM" in stations
    assert "BBC RADIO 1" in stations

    # Ensure comment block was skipped.
    assert "IgnoreMe" not in stations

    # Validate fields
    assert stations["ROCK FM"]["url"] == "http://rock.fm/stream"
    assert stations["ROCK FM"]["category"] == "ROCK"
    assert stations["ROCK FM"]["country"] == "US"

    # Category defauly
    assert stations["JAZZ FM"]["category"] == "Unknown"

    # UK station
    assert stations["BBC RADIO 1"]["country"] == "UK"