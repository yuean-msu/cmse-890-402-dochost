# Tutorial

Hello and welcome to my site for the package `qiu`! This page will use some examples to guide you through the `qiu` package to support your own project!

## Setup
First install the package by running:
```
pip install qiu
```

And then in python import the package.
```
import qiu
```

## Rectangle
In the world of geometry, rectangle is one of the most basic shapes. Normally, we would create a rectangle by first defining its width and height.

```
width = 5
height = 10
```

Then the next step is to learn about its properties, including perimeter and area.

```
perimeter = qiu.cal_perimeter_of_rectangle(width, height)
area = qiu.cal_area_of_rectangle(width, height)
```

Print the results:
```
print(perimeter) # 30
print(area) # 50
```

## Summary
Now you should know how to use the `qiu` package: import it and call its function. There are some other useful functions in it. Explore more on the "How-to" page!
