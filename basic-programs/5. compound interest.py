# Formula for CI
# A = P(1 + R/100) t 
# Compound Interest = A – P 

# Where, 
# A is amount 
# P is the principal amount 
# R is the rate and 
# T is the time span

def CI(p, t, r):
    amount = p * pow((1 + (r / 100)) , t)
    return amount - p
    
p = int(input("Enter Principal: "))
t = int(input("\n Enter Time Period: "))
r = int(input("\n Enter Rate of Interest: "))

print("CI of {0}, {1} and {2} is {3}".format(p, t, r, CI(p,t,r)))