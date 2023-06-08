def solar_irradiance(area, power):
    """
    Calculates the solar irradiance in W/m^2 given the area and power of
    a PV module.
    """
    return power / area

def pv_module_efficiency(power_output, solar_irradiance):
    """
    Calculates the efficiency of a PV module given the power output and
    solar irradiance.
    """
    return power_output / (solar_irradiance * area)

def power_output(area, solar_irradiance, pv_module_efficiency):
    """
    Calculates the power output of a PV module given the area, solar
    irradiance, and efficiency.
    """
    return area * solar_irradiance * pv_module_efficiency
