# Recursion = is the process of repeating items in a self-similar way
# multiplying a,b using iteration
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

# by recursion
#a * b = a+a+a+a+a+a .... +a(b times)
# a +a*(b-1)
def multi(a,b):
    if b == 1:
        return a
    else:
        return a + multi(a, b-1)
a = int(input("Please Input the value of a: "))
b = int(input("Please input the value of b: "))
result = multiply(a,b)
print(f"The result of {a} * {b} = {result}")


# factoral using recursive
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))