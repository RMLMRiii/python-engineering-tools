# Simple force component calculator

import math

def force_components(force, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    fx = force * math.cos(angle_radians)
    fy = force * math.sin(angle_radians)
    return fx, fy

force = 100
angle = 30

fx, fy = force_components(force, angle)

print(f"Force: {force} N")
print(f"Angle: {angle} degrees")
print(f"Fx = {fx:.2f} N")
print(f"Fy = {fy:.2f} N")
