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