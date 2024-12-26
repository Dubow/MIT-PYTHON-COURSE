# Tuples= They are immutable(once created cannot be changed)
# Tuples are created using parenthesis()
t = (2, "sut", 10)
print(t[0]) #prints out 2
x = (2, "mit", 10)+(5,6)
print(x) #prints out the added list

def quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return q,r
(x,y) = (4,3)
result = quotient_and_remainder(x,y)
print(result)

# List = they are mutable(can be changed/altered)
# they are created using brackets[]
a_list = []#empty list
L = [2, 4, 5, "sad", "happy", 37]
L[5] = 32
L.append(55) # add 55 to the list L
print(len(L), L[4], L) #prints out the length of L and the index 2 element
x = [2,35,67,45,67]
total = 0
for i in range(len(x)):
    total += x[i]
print(total) # prints out the sum of list x

# combining list
L1 = [1,2,3,4,5]
L1.extend([-1,0]) # add -1 and 0 to L1
L1.remove(2) #removes 2 from list L1
L2 = [6,7,8,9,10]
L2.pop() # removes the last number
L3 = L1 + L2
print(L3) # prints out the combined lists

# converting list to strings and viceversa
s = "I < CS" # s is a string
print(list(s)) # prints out ['I', ' ', '<', ' ', 'C', 'S']
print(s.split('<')) #removes '<' from the list
a = ['A','B','C']
print(''.join(a)) #joins the whole list prints out ABC
print('_'.join(a))#joins the whole list while adding '_'in between each  A_B_C

#sorting and reversing
worm = ["red", "yellow", "orange"]
sortedWorm = worm.sort()
print(worm)
print(sortedWorm)

#clonning list in python
cool = ["blue", "Green","White"]
chill = cool[:] #[:]clones all the elements in cool list
cool.append("black")
print(cool)
print(chill)

color = ["pink", "indigo"]
extras = ["yellow"]
brightcolors = [color]
brightcolors.append(extras)
print(brightcolors)