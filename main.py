import requests

# Documentation metaweather:
# https://www.metaweather.com/api/


_URL = 'https://www.metaweather.com/api/location/'

def get_weather_state_by_location(location):
  # Get the woeid
  location_id = str(
    requests.get(_URL + 'search/?query=' + location).json()[0]['woeid'])

  # Weather and weather state
  weather = requests.get(_URL + location_id +'/').json()
  weather_state = weather['consolidated_weather'][0]['weather_state_name']
  return weather_state


def get_weather_state_by_woeid(location_id):
  # Weather and weather state
  weather = requests.get(_URL + location_id +'/').json()
  weather_state = weather['consolidated_weather'][0]['weather_state_name']
  return weather_state

# Log
print 'weather state: %s' % get_weather_state_by_location('seattle')
print 'weather state: %s' % get_weather_state_by_woeid('2490383')

# TODO(cnishina): Convert to functions and add testing.
# TODO(cnishina): Add option to write to file.