# Simple engineering unit converter

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

value_meters = 10
value_feet = 10

print(f"{value_meters} meters = {meters_to_feet(value_meters):.2f} feet")
print(f"{value_feet} feet = {feet_to_meters(value_feet):.2f} meters")
