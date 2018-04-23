import requests

# Documentation metaweather based on Todd Moto:
# https://www.metaweather.com/api/

_URL = 'https://www.metaweather.com/api/location'


def get_woeid(location):
  # Get the woeid.
  #
  # Args:
  #   location: The city name.
  #
  # Returns:
  #   A number associated with the location woeid.
  url = '%s/search/?query=%s' % (_URL, location)
  return requests.get(url).json()[0]['woeid']


def get_weather_state(woeid):
  # Get the weather state.
  #
  # Args:
  #   woeid: The woeid number for the city.
  #
  # Returns:
  #   A string describing the weather state.
  url = '%s/%d/' % (_URL, woeid)
  weather = requests.get(url).json()
  return weather['consolidated_weather'][0]['weather_state_name']