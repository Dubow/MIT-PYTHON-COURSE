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

# fibonnaci using recursive
def feb(n):
    if n == 0:
        return 0   #base case
    elif n == 1:
        return 1   #base case
    else:
        return feb(n-1)+feb(n-2)
n = int(input("Please enter your preffered number: "))
result = feb(n)
print(f"The fibonnaci result for {n} is {result}")

# Dictionaries
# dictionary is created using curly braces{}
#my_dict = {} #empty dictionary
grades = {'Anna':'B','John':'A','Denise':'A+','Abdi':'A'}
print(grades['Anna']) #prints out B
# adding an entry into the dictionary
grades['Kate'] = 'A'
print('Mathews' in grades) #Tests if mathews is in the dictionary
# deleting entries
del(grades['Anna'])
print(grades.keys()) #printout all dict_keys
print(grades.values()) #prints out all values

she_loves_you = ['she','loves','you','yeah','she','loves','you','yeah','yeah']

def lyrics_to_frequence(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict
print(lyrics_to_frequence(she_loves_you))
