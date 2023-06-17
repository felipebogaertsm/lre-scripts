from services.flow import (
    total_flow,
    fuel_flow_from_of_ratio,
    oxidizer_flow_from_of_ratio,
    throat_area_from_mass_flow,
)
from services.isentropic import temperature_at_throat, pressure_at_throat

# TARGETS
THRUST_DESIRED = 89  # Newtons
CHAMBER_PRESSURE = 2.068e6  # Pascals

# CONSTANTS
I_SP = 260  # seconds
GAMMA = 1.2  # unitless
MOLAR_MASS_PROPELLANT = 0.023  # kg/mol

# PROPELLANT FLOW
OF_RATIO = 2.5
MASS_FLOW_TOTAL = total_flow(thrust=THRUST_DESIRED, i_sp=I_SP)  # kg/s
FUEL_FLOW = fuel_flow_from_of_ratio(
    of_ratio=OF_RATIO, total_flow=MASS_FLOW_TOTAL
)  # kg/s
OX_FLOW = oxidizer_flow_from_of_ratio(
    of_ratio=OF_RATIO, total_flow=MASS_FLOW_TOTAL
)  # kg/s

print(f"Total mass flow: {MASS_FLOW_TOTAL:.3f} kg/s")
print(f"Fuel flow: {FUEL_FLOW:.3f} kg/s")
print(f"Oxidizer flow: {OX_FLOW:.3f} kg/s")
print(f"Oxidizer to fuel ratio: {OX_FLOW / FUEL_FLOW:.3f}")

# THERMALS
CHAMBER_TEMP = 3445  # Kelvin
GAS_TEMP_AT_THROAT = temperature_at_throat(
    chamber_temperature=CHAMBER_TEMP, gamma=GAMMA
)  # Kelvin
PRESSURE_AT_THROAT = pressure_at_throat(
    chamber_pressure=CHAMBER_PRESSURE, gamma=GAMMA
)  # Pascals

print(f"Chamber temperature: {CHAMBER_TEMP:.3f} K")
print(f"Gas temperature at throat: {GAS_TEMP_AT_THROAT:.3f} K")
print(f"Pressure at throat: {PRESSURE_AT_THROAT * 1e-6:.3f} MPa")

# NOZZLE
THROAT_AREA = throat_area_from_mass_flow(
    mass_flow=MASS_FLOW_TOTAL,
    pressure=PRESSURE_AT_THROAT,
    temperature=GAS_TEMP_AT_THROAT,
    gamma=GAMMA,
    molar_mass=MOLAR_MASS_PROPELLANT,
)  # m^2

print(f"Throat area: {THROAT_AREA * 1e6:.3f} cm^2")
