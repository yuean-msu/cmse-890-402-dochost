from typing import Union

def cal_area_of_rectangle(width: Union[float, int], height: Union[float, int]) -> Union[float, int]:
    """Calculate the area of a rectangle
    
    It is a very basic function for rectangle.

    Args:
        width (Union[float, int]): width of the rectangle.
        height (Union[float, int]): height of the rectangle.

    Returns:
        The area = width * height.
    """
    
    area = width * height
    return area