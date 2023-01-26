# Get the number of digits in the number
def getDigitsCount(n):
    count = 0

    while n > 0:
        r = n % 10
        n = n // 10 # Floor division
        count += 1

    return count

# Function to calculate x raised to the power y
def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)

    return x * power(x, y // 2) * power(x, y // 2)

# Function to check whether the given number is Armstrong or not
def isArmstrong(n):

    digits = getDigitsCount(n)
    temp = n
    sum1 = 0

    while temp > 0:
        r = temp % 10
        sum1 = sum1 + power(r, digits)
        temp = temp // 10

    return sum1 == n 


# Driver code
x = 153
print(isArmstrong(x))
 
x = 1253
print(isArmstrong(x))
