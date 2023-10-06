def my_thermo_stat(temp: int, desired_temp: int) -> str:
    """Changes the status of the thermostat based on temperature and desired temperature
    
    If the temperature is 5 degrees apart from the desired temperature, report the status.
    
    Args:
        temp: the current temperature, int.
        desired_temp: the desired temperature, int.
    
    Returns:
        The thermostat status, values include 'Heat', 'AC', and 'off'.
    
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status
    