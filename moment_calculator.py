# Simple moment calculator

def moment(force, distance):
    return force * distance

force = 250      # N
distance = 3.0   # m

calculated_moment = moment(force, distance)

print(f"Force: {force} N")
print(f"Distance: {distance} m")
print(f"Moment: {calculated_moment:.2f} N·m")
