# use the 'class' keyword to define a new type
class sample():
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
c = sample()
n = int(input("please enter the value of n: "))
result = c.fib(n)
print(f"The {n}-th Fibonnuci number is {result}")