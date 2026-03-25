# Simple stress and strain calculator

def stress(force, area):
    return force / area

def strain(change_in_length, original_length):
    return change_in_length / original_length

force = 5000           # N
area = 0.002           # m^2
change_in_length = 0.001
original_length = 2.0  # m

calculated_stress = stress(force, area)
calculated_strain = strain(change_in_length, original_length)

print(f"Force: {force} N")
print(f"Area: {area} m^2")
print(f"Stress: {calculated_stress:.2f} Pa")
print(f"Strain: {calculated_strain:.6f}")
