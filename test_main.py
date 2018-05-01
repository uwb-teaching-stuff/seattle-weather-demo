import main

def test_temperature_celcius():
    temp = float(main.get_temp())
    assert temp > 7
    assert temp < 30


def test_location_id_for_seattle():
    assert main.get_location_id() == "2490383";