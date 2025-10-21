import requests
import time

url = "https://external.transitapp.com/v3/map_layers/available_networks"

params = {
    'lat': 38.9918559108366,
    'lon': -76.94503827610498,
    'max_distance': 1500,
    'locale': 'en',
    'should_update_realtime': 'true',
    'max_num_departures': 3,
    'time': time.time(),
    'include_stops_and_shapes': 'true'
}

headers = {
    'apiKey': 'apiKey'
}

try:
    response = requests.get(url, params=params, headers=headers)
    print(url+"?"+str(params))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}...")  # First 500 chars
except Exception as e:
    print(f"Error: {e}")