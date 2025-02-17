"""
Design calculations for a liquid rocket engine.

References:
https://spacha.github.io/How-to-Rocket/
Accessed at 2025-02-15 15:34Z
"""

import cantera as ct

from services.flow import (
    fuel_flow_from_of_ratio,
    fuel_spray_injector_area,
    oxidizer_flow_from_of_ratio,
    throat_area_from_mass_flow,
    total_flow,
)
from services.geometric import area_to_diameter, diameter_to_area
from services.isentropic import (
    optimal_expansion_ratio,
    pressure_at_throat,
    temperature_at_throat,
)
from services.schemas import load_inputs


def main() -> None:
    """Main function to execute design calculations for a liquid rocket engine."""

    # Auto-load inputs dynamically for this script
    inputs = load_inputs("preliminary_design")

    # STEP 1 - Compute Mass Flow Rates
    mass_flow_total = total_flow(thrust=inputs.thrust_desired, i_sp=inputs.isp)  # kg/s
    fuel_flow = fuel_flow_from_of_ratio(
        of_ratio=inputs.of_ratio, total_flow=mass_flow_total
    )
    oxidizer_flow = oxidizer_flow_from_of_ratio(
        of_ratio=inputs.of_ratio, total_flow=mass_flow_total
    )

    print(f"Total mass flow: {mass_flow_total:.4f} kg/s")
    print(f"Fuel flow: {fuel_flow:.4f} kg/s")
    print(f"Oxidizer flow: {oxidizer_flow:.4f} kg/s")
    print(f"Oxidizer to fuel ratio: {oxidizer_flow / fuel_flow:.4f}")

    # STEP 2 - Compute Gas Properties at the Throat
    gas_temp_at_throat = temperature_at_throat(
        chamber_temperature=inputs.chamber_temperature, gamma=inputs.gamma
    )

    print(f"Chamber temperature: {inputs.chamber_temperature:.4f} K")
    print(f"Gas temperature at throat: {gas_temp_at_throat:.4f} K")

    # STEP 3 - Compute Pressure at the Throat
    pressure_at_throat_value = pressure_at_throat(
        chamber_pressure=inputs.chamber_pressure, gamma=inputs.gamma
    )

    print(f"Pressure at throat: {pressure_at_throat_value * 1e-6:.4f} MPa")

    # STEP 4 - Compute Throat Area
    throat_area = throat_area_from_mass_flow(
        mass_flow=mass_flow_total,
        pressure=pressure_at_throat_value,
        temperature=gas_temp_at_throat,
        gamma=inputs.gamma,
        molar_mass=inputs.molar_mass_propellant,
    )

    print(f"Throat area: {throat_area * 1e4:.4f} cm^2")

    # STEP 5 - Compute Throat Diameter
    throat_diameter = area_to_diameter(area=throat_area)

    print(f"Throat diameter: {throat_diameter * 1e3:.4f} mm")

    # STEP 6 - Compute Optimal Expansion Ratio and Exit Area
    optimal_er = optimal_expansion_ratio(
        chamber_pressure=inputs.chamber_pressure,
        atmospheric_pressure=inputs.atmospheric_pressure,
        gamma=inputs.gamma,
    )
    exit_area = throat_area * optimal_er

    print(f"Optimal expansion ratio: {optimal_er:.4f}")
    print(f"Exit area: {exit_area * 1e4:.4f} cm^2")

    # STEP 7 - Compute Exit Diameter
    exit_diameter = area_to_diameter(exit_area)
    print(f"Exit diameter: {exit_diameter * 1e3:.4f} mm")

    # STEP 8 - Compute Chamber Volume
    chamber_volume = inputs.l_star * throat_area

    print(f"Chamber volume: {chamber_volume * 1e6:.4f} L")

    # STEP 9 - Compute Chamber Dimensions
    chamber_diameter = 5 * throat_diameter
    chamber_length = chamber_volume / (
        diameter_to_area(diameter=chamber_diameter) * 1.1
    )

    print(f"Chamber diameter: {chamber_diameter * 1e3:.4f} mm")
    print(f"Chamber length: {chamber_length * 1e3:.4f} mm")

    # STEP 10 - Compute Chamber Wall Thickness
    chamber_wall_thickness = (inputs.chamber_pressure * chamber_diameter) / (
        2 * inputs.chamber_yield_strength / inputs.safety_factor
    )

    print(f"Chamber wall thickness: {chamber_wall_thickness * 1e3:.4f} mm")

    # STEP 14 - Compute Fuel Injector Area
    fuel_injector_area = fuel_spray_injector_area(
        flow=fuel_flow,
        orifice_discharge_coefficient=inputs.injector_orifice_discharge_coefficient,
        density=inputs.fuel_density,
        pressure_drop=inputs.fuel_pressure_drop,
    )

    print(f"Fuel injector area: {fuel_injector_area * 1e6:.4f} mm^2")

    # STEP 15 - Compute Oxidizer Injector Area
    gas = ct.Solution("air.yaml")
    gas.TP = (
        inputs.ambient_temperature,
        inputs.chamber_pressure + inputs.oxidizer_pressure_drop,
    )
    gas.X = {inputs.oxidizer_name: 1.0}  # Define pure oxidizer composition

    oxidizer_density_at_entrance = gas.density
    oxidizer_injector_area = oxidizer_flow / (
        oxidizer_density_at_entrance * inputs.oxidizer_velocity
    )

    print(
        f"Oxidizer pressure at entrance: {(inputs.chamber_pressure + inputs.oxidizer_pressure_drop) * 1e-6:.4f} MPa"
    )
    print(f"Oxidizer density at entrance: {oxidizer_density_at_entrance:.4f} kg/m^3")
    print(f"Oxidizer injector area: {oxidizer_injector_area * 1e6:.4f} mm^2")


if __name__ == "__main__":
    main()
