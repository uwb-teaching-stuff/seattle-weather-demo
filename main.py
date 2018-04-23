import requests

# Documentation metaweather:
# https://www.metaweather.com/api/


_URL = 'https://www.metaweather.com/api/location/'

def get_woid(location):
  # Get the woeid
  location_id = str(
    requests.get(_URL + 'search/?query=' + location).json()[0]['woeid'])
  return location_id


# Log
print 'weather state: %s' % get_woid('seattle')

# TODO(cnishina): Convert to functions and add testing.
# TODO(cnishina): Add option to write to file.