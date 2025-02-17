from pydantic import BaseModel, Field


class ScriptInputs(BaseModel):
    thrust_desired: float = Field(..., description="Target thrust in Newtons")
    chamber_pressure: float = Field(..., description="Chamber pressure in Pascals")
    l_star: float = Field(..., description="Characteristic chamber length in meters")
    i_sp: float = Field(..., description="Specific impulse in seconds")
    gamma: float = Field(..., description="Ratio of specific heats")
    molar_mass_propellant: float = Field(
        ..., description="Molar mass of propellant in kg/mol"
    )
    atmospheric_pressure: float = Field(..., description="Ambient pressure in Pascals")
    chamber_yield_strength: float = Field(
        ..., description="Chamber material yield strength in Pascals"
    )
    safety_factor: float = Field(..., description="Design safety factor")
    injector_orifice_discharge_coefficient: float = Field(
        ..., description="Injector discharge coefficient"
    )
    fuel_density: float = Field(..., description="Fuel density in kg/m^3")
    fuel_pressure_drop: float = Field(..., description="Fuel pressure drop in Pascals")
    ox_pressure_drop: float = Field(
        ..., description="Oxidizer pressure drop in Pascals"
    )
    ox_velocity: float = Field(..., description="Oxidizer injection velocity in m/s")
    ox_name: str = Field(..., description="Oxidizer chemical name")
    ambient_temperature: float = Field(..., description="Ambient temperature in Kelvin")
    of_ratio: float = Field(..., description="Oxidizer-to-Fuel mass ratio")
    chamber_temp: float = Field(..., description="Chamber temperature in Kelvin")
