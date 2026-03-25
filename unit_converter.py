# Simple engineering unit converter

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

print("10 meters =", meters_to_feet(10), "feet")
print("10 feet =", feet_to_meters(10), "meters")
