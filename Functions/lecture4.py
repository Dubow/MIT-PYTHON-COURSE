# Lecture 4: Decomposition, Abstraction, and Functions
# look for whether the number is even or not
def is_even(number):
    if number % 2 == 0:
        return('even number')
    else:
        return('odd number')
number = int(input("Input your number please: "))
result = is_even(number)
print(f"The number {number} is an {result}")