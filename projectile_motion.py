# Simple projectile motion calculator

import math

def projectile_range(velocity, angle_degrees, gravity=9.81):
    angle_radians = math.radians(angle_degrees)
    return (velocity ** 2 * math.sin(2 * angle_radians)) / gravity

velocity = 20
angle = 45

range_distance = projectile_range(velocity, angle)

print(f"Initial velocity: {velocity} m/s")
print(f"Launch angle: {angle} degrees")
print(f"Projectile range: {range_distance:.2f} meters")
