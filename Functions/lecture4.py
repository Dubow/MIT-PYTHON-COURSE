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


# reversing a word
def reversed_word(word):
    reversed_word = word[::-1]
    return reversed_word
word = 'I love you'
result = reversed_word(word)
print(f"The reversed word of '{word}' is '{result}'")


# palindrome
def isPalindrome(x: int):
    if x < 0:
        return False
    x_str = str(x) # converts the number to a string
    return x_str == x_str[::-1]
x = 1221
result=(isPalindrome(x))
print(f"The number '{x}' is a palindrome: {result}")