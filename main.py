import metaweather


# Sample code with logging
woeid = metaweather.get_woeid('seattle')
print 'location id: %s' % woeid
print 'weather state: %s' % metaweather.get_weather_state(woeid)