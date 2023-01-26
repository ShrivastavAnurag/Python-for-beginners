# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.

def factorial(n):
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)

num1 = 5

print("factorial of {0} is {1}".format(num1,factorial(num1)))
