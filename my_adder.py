from typing import Union

def my_adder(a: Union[float, int], b: Union[float, int], c: Union[float, int]) -> Union[float, int]:
    """Add three numbers
    
    This function is simply to sum the 3 numbers.
    
    Args: 
        a: the 1st number, either float or int.
        b: the 2nd number, either float or int.
        c: the 3rd number, either float or int.
    
    Returns:
        The sum of a, b, and c. If input are all int, return is int; otherwise, return is float.
    
    """
    
    # this is the summation
    out = a + b + c
    
    return out
