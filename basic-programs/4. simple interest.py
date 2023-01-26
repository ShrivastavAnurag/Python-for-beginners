# Formula for SI
# SI = (P * T * R) / 100

# Where,  
# P is the principal amount 
# R is the rate and 
# T is the time span

def SI(p, t, r):
    return (p * t * r) / 100

p = int(input("Enter Principle: "))
t = int(input("\n Enter Time period: "))
r = int(input("\n Enter Rate of interest: "))

print("SI of {0}, {1} and {2} is {3}".format(p,t,r,SI(p,t,r)))
