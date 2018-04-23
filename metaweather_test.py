import unittest
import mock
from mock import MagicMock

import metaweather

_WOEID = 12345
_LOCATION = 'foobar'

def mocked_request_get(*args, **keywargs):
  class MockResponse:
    def __init__(self, json_data, status_code):
      self.json_data = json_data
      self.status_code = status_code

    def json(self):
      return self.json_data

  if '/search/?query' in args[0]:
    # Query by city
    return MockResponse([{'woeid': 'value1'}], 200)
  elif ('/%d' % _WOEID) in args[0]:
    # Get weather state
    return MockResponse(
      {'consolidated_weather': [{'weather_state_name': 'BAD WEATHER!'}]}, 200)

  return MockResponse(None, 400)


class TestMetaWeather(unittest.TestCase):
  
  @mock.patch('requests.get', side_effect=mocked_request_get)
  def test_get_woeid(self, mock_get):
    self.assertEquals(metaweather.get_woeid(_LOCATION), 'value1')

  @mock.patch('requests.get', side_effect=mocked_request_get)
  def test_get_weather_state(self, mock_get):
    self.assertEquals(metaweather.get_weather_state(_WOEID), 'BAD WEATHER!')

if __name__ == '__main__':
  unittest.main()