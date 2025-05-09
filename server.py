import json

from geopy.geocoders import Nominatim
from datetime import datetime
from meteostat import Point, Daily
import zmq

context = zmq.Context()

socket = context.socket(zmq.REP)

socket.bind("tcp://*:5555")


def get_lat_lon(location_name):
    geolocator = Nominatim(user_agent="location-to-coordinates")
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


def get_data(lat, lon, start_day, start_month, start_year, end_day, end_month, end_year):
    location = Point(lat, lon)
    date_start = datetime(start_year, start_month, start_day)
    date_end = datetime(end_year, end_month, end_day)

    data = Daily(location, date_start, date_end)
    data = data.fetch()

    return data['tavg'].mean()


while True:
    # Receive and decode message
    message = socket.recv_string()
    print(f"Received request: {message}")

    # Parse JSON data
    try:
        data = json.loads(message)
        address = data['address']
        start_day = data['start_day']
        start_month = data['start_month']
        start_year = data['start_year']
        end_day = data['end_day']
        end_month = data['end_month']
        end_year = data['end_year']

        lat, lon = get_lat_lon(address)
        if lat and lon:
            avg_temp = get_data(lat, lon, start_day, start_month, start_year, end_day, end_month, end_year)
            response = {
                "status": "success",
                "location": address,
                "average_temperature": round(avg_temp)
            }
        else:
            response = {"status": "error", "message": "Location not found"}
    except Exception as e:
        response = {"status": "error", "message": str(e)}

    # Send response back to client
    socket.send_string(json.dumps(response))

