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
L[4] = 32
print(len(L), L[4], L) #prints out the length of L and the index 2 element