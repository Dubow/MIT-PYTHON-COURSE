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

# adding arrays  from codewars
def sum_array(a):
    if not a:
        return 0
    return sum(a)
a = [1,3,5,7]
result = sum_array(a)
print(f"The sum of '{a}' is '{result}'")

# codewars quiz
def rental_car_cost(d):
    daily_rate = 40
    total = d * daily_rate
    if d >=7:
        return total - 50
    elif d>=3:
        return total - 20
    return total
    
d = int(input("input the number of days: "))
result = rental_car_cost(d)
print(f"The total amount for {d} days of rental fee is {result}")


# leetcode quiz
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def twoSum(nums: int, target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
    return []
nums,target = [1,2,3,4,5,6,9], 9
result = twoSum(nums,target)
print(f"The indices for the targrt number is '{result}'")