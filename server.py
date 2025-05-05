from geopy.geocoders import Nominatim
from datetime import datetime
from meteostat import Point, Daily


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


# Example usage:
address = input("Enter a location: ")
lat, lon = get_lat_lon(address)

if lat and lon:
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("Location not found.")

data = get_data(lat, lon, start_day=1, start_month=1, start_year=2019, end_day=1, end_month=1, end_year=2023)

print(f"5-Year Average Temperature: {data:.2f} °C")
