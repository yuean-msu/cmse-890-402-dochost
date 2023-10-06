# How-to

## How to add three numbers

Given three numbers, either int or float, how to use `qiu` to add them in one line?
Use `my_adder()`.

```
a = 1
b = 2
c = 3
sum = qiu.my_adder(a, b, c)
print(sum) # 6
```

You can even mix the types of input!
```
a = 1
b = 2
c = 3.0
sum = qiu.my_adder(a, b, c)
print(sum) # 6.0
```

## How to get thermo status

Given the current temperature and a desired temperature, how to get the status of your thermo? 
`Use my_thermo_stat()`

```
temp = 32
desired_temp = 26
stat = my_thermo_stat(temp, desired_temp)
print(stat) # 'AC'
```