import math

# Function to check if number if prime or not
def isPrimeNumber(n):

    if n > 1:
        sqrtNum = int(math.sqrt(n))
        primeFlag = 0
        
        for i in range(2, sqrtNum+1):
            if n % i == 0:
                primeFlag = 1
                break
            
        if primeFlag:
            return 0
        else:
            return 1
    else:
        return 0

# Function to get list of prime numbers
def findPrime (x, y):
    primeList = []

    for i in range(x, y):
        if i <= 0:
            continue
        else:
            if isPrimeNumber(i):
                primeList.append(i)
    return primeList

startingRange = int(input("Enter Starting Range: "))
endingRange = int(input("Enter Ending Range: "))

primeList = findPrime(startingRange, endingRange)

if len(primeList):
    print("The prime numbers in {0} and {1} are: {2}".format(startingRange, endingRange, primeList))
else:
    print("There are no prime numbers in {0} and {1}".format(startingRange, endingRange))