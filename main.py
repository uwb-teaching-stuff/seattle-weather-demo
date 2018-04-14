import requests

_URL = 'https://www.metaweather.com/api/location/'

print requests.get(_URL + 'search/?query=seattle').json()

location_id = str(requests.get(_URL + 'search/?query=seattle').json()[0]['woeid'])

print requests.get(_URL + location_id +"/").json()['consolidated_weather'][0]['weather_state_name']