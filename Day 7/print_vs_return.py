def add(a, b):
    return a + b

sum = add(1, 2)   # sum now holds the value 3
print(sum)        # you decide when/how to display it
print(sum * 10)   # you can reuse the value: prints 30

def add(a, b):
    print(a + b)   # displays 3 immediately, but gives nothing back

result = add(1, 2)   # result is None! the function didn't return anything
print(result)        # prints: None
print(result * 10)   # ERROR: can't multiply None by 10