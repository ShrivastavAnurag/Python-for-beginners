import math

def isPrimeNumber(n):

    if n > 1:
        sqrtNum = int(math.sqrt(n))
        primeFlag = 0
        
        for i in range(2, sqrtNum+1):
            if n % i == 0:
                primeFlag = 1
                break
            
        if primeFlag == 0:
            print("True")
        else:
            print("False")    
    else:
        print("False")

n = int(input("Enter Number: "))

isPrimeNumber(n)
