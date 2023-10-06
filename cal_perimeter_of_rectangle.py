from typing import Union

def cal_perimeter_of_rectangle(width: Union[float, int], height: Union[float, int]) -> Union[float, int]:
    """Calculate the perimeter  of a rectangle
    
    It is a very basic function for rectangle.

    Args:
        width (Union[float, int]): width of the rectangle.
        height (Union[float, int]): height of the rectangle.

    Returns:
        The perimeter = 2 * (width + height).
    """
    
    perimeter = 2 * (width + height)
    return perimeter