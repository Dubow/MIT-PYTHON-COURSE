# Recursion = is the process of repeating items in a self-similar way
# multiplying a,b using recursion
def multiply(a,b):
    result = 0   #initializes the base to be 0
    while b > 0:
        result += a
        b -=1
    return result
a = int(input("Please Input the value of a: "))
b = int(input("Please input the value of b: "))
result = multiply(a,b)
print(f"The result of {a} * {b} = {result}")