from services.flow import (
    total_flow,
    fuel_flow_from_of_ratio,
    oxidizer_flow_from_of_ratio,
    throat_area_from_mass_flow,
)
from services.geometric import area_to_diameter, diameter_to_area
from services.isentropic import (
    temperature_at_throat,
    pressure_at_throat,
    optimal_expansion_ratio,
)

# TARGETS AND CONSTANTS
THRUST_DESIRED = 89  # Newtons
CHAMBER_PRESSURE = 2.068e6  # Pascals
L_STAR = 1.52  # meters
I_SP = 260  # seconds
GAMMA = 1.2  # unitless
MOLAR_MASS_PROPELLANT = 0.023  # kg/mol
ATMOSPHERIC_PRESSURE = 101325  # Pascals
CHAMBER_YIELD_STRENGTH = 55.2e6  # Pascals
SAFETY_FACTOR = 3  # unitless

# STEP 1
OF_RATIO = 2.5
mass_flow_total = total_flow(thrust=THRUST_DESIRED, i_sp=I_SP)  # kg/s
fuel_flow = fuel_flow_from_of_ratio(
    of_ratio=OF_RATIO, total_flow=mass_flow_total
)  # kg/s
ox_flow = oxidizer_flow_from_of_ratio(
    of_ratio=OF_RATIO, total_flow=mass_flow_total
)  # kg/s

print(f"Total mass flow: {mass_flow_total:.3f} kg/s")
print(f"Fuel flow: {fuel_flow:.3f} kg/s")
print(f"Oxidizer flow: {ox_flow:.3f} kg/s")
print(f"Oxidizer to fuel ratio: {ox_flow / fuel_flow:.3f}")

# STEP 2
CHAMBER_TEMP = 3445  # Kelvin
gas_temp_at_throat = temperature_at_throat(
    chamber_temperature=CHAMBER_TEMP, gamma=GAMMA
)  # Kelvin

print(f"Chamber temperature: {CHAMBER_TEMP:.3f} K")
print(f"Gas temperature at throat: {gas_temp_at_throat:.3f} K")

# STEP 3
pressure_at_throat = pressure_at_throat(
    chamber_pressure=CHAMBER_PRESSURE, gamma=GAMMA
)  # Pascals

print(f"Pressure at throat: {pressure_at_throat * 1e-6:.3f} MPa")

# STEP 4
throat_area = throat_area_from_mass_flow(
    mass_flow=mass_flow_total,
    pressure=pressure_at_throat,
    temperature=gas_temp_at_throat,
    gamma=GAMMA,
    molar_mass=MOLAR_MASS_PROPELLANT,
)  # m^2

print(f"Throat area: {throat_area * 1e4:.3f} cm^2")

# STEP 5
throat_diameter = area_to_diameter(area=throat_area)  # m

print(f"Throat diameter: {throat_diameter * 1e3:.3f} mm")

# STEP 6
optimal_er = optimal_expansion_ratio(
    chamber_pressure=CHAMBER_PRESSURE,
    atmospheric_pressure=ATMOSPHERIC_PRESSURE,
    gamma=GAMMA,
)
exit_area = throat_area * optimal_er  # m^2

print(f"Optimal expansion ratio: {optimal_er:.3f}")
print(f"Exit area: {exit_area * 1e4:.3f} cm^2")

# STEP 7
exit_diameter = area_to_diameter(exit_area)  # m
print(f"Exit diameter: {exit_diameter * 1e3:.3f} mm")

# STEP 8
chamber_volume = L_STAR * throat_area  # m^3

print(f"Chamber volume: {chamber_volume * 1e6:.3f} L")

# STEP 9
chamber_diameter = 5 * throat_diameter  # m
chamber_length = chamber_volume / (
    diameter_to_area(diameter=chamber_diameter) * 1.1
)  # m

print(f"Chamber diameter: {chamber_diameter * 1e3:.3f} mm")
print(f"Chamber length: {chamber_length * 1e3:.3f} mm")

# STEP 10
chamber_wall_thickness = (CHAMBER_PRESSURE * chamber_diameter) / (
    2 * CHAMBER_YIELD_STRENGTH / SAFETY_FACTOR
)

print(f"Chamber wall thickness: {chamber_wall_thickness * 1e3:.3f} mm")
