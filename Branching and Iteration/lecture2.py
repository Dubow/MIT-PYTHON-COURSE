# strings
name = "Dubow"
hi = "Hello there"
greet = hi + name
print(greet) #it will print without a space "Hello thereDubow"
greeting = hi + " " + name
print(greeting) #prints with space since we added the " "

# control flow if ... else
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
if x==y:
    print("x and y are equal")
elif x > y:
    print("x is greater than y")
else:
    print("y is greater than x")
print("Thank you")

# control flow while loop used when you have unbounded number of iterations

n = input("You are in the lost forest go left or right: ")
while n == "right":
    n = input("You are in the lost forest go left or right: ")
print("you are out of the forest")

# for loop used when you know the range

n = 0
for i in range(5, 9, 2):
    n += i
    print(n)