# A Very Simple Program: Raising a number to a power and taking a logarithm 
 
 
# The goal of this programming exercise is to make sure your python and numpy installations 
# are correct, to get you more comfortable with using Spyder, and to begin using simple 
# elements of Python. Standard elements of a program include the ability to print out results 
# (using the print operation), the ability to read input from a user at the console (for 
# example using the input function), and the ability to store values in a variable, so that the 
# program can access that value as needed. 

## Assignment: 
 
#  Write a program that does the following in order: 
 
# 1. Asks the user to enter a number “x” 
# 2. Asks the user to enter a number “y” 
# 3. Prints out number “x”, raised to the power “y”. 
# 4. Prints out the log (base 2) of “x”. 

import math # Importing the math module for mathematical operations

x = int(input("Enter the value of x: ")) #Asking the user to enter the value of 'x'
y = int(input("Enter the value of y: ")) #Asking the user to enter the value of 'y'
result = x ** y #getting the result “x”, raised to the power “y”.
print(f"The result of {x} ** {y} is {result}")

# Calculate and print the log base 2 of "x"
if x > 0:
    log_base = math.log2(x)
    print(f"The log base 2 of {x} is {log_base}")
else:
    print("Logarithm is undefined for non-positive values.")