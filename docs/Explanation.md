# Explanation

## Switching arguments
Why in some functions like `cal_area_of_rectangle()` or `my_adder()`, the arguments are interchangeable, but in functions like `thermo_stat()`, they are not?

Well, for the calculation of area or perimeter of rectangles, width and height play the same role if you look at the formula: `area = width * height` and `perimeter = 2 * (width + height)`. Similarly, in `my_adder()`, the order of the three input numbers doesn't matter thanks to the law of math.

However, in `thermo_stat()`, one need to compare the two input arguments, so you must know which is which!