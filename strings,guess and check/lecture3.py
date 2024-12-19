#  String Manipulation, Guess and Check, Approximations, Bisection
s = 'abcdefhg' #string
print(len(s)) # getting the length of string s
print(s[2:5:2]) # getting the position since the index in python starts from 0 and -1 from the last #[start:stop:step]
word = 'Hello World!'
print(word[::-1]) # reverses the whole word

# strings are immutable
x = "hello"
x = 'y' + x[1:len(x)] #adds 'y' to the string and ommits 'h' since it is startiong from index 1
print(x)

# for loop strings
a = 'abcdefghijklmnRXHJYZG'
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthuisum level 1-10: "))
i=0
for char in word:
    if char in a:
        print("Give me an " + char + " ! " + char)
    else:
        print("Give me a " + char + " ! " + char)
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

