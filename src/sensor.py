from w1thermsensor import W1ThermSensor

def get_temperature_celsius():
    sensor = W1ThermSensor()
    return sensor.get_temperature()