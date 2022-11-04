"""
A program that will calculate the greatest common denominator of
two given numbers using the Euclidean Algoirithm showing all work.
Author: Dalton Kohl
Date Last Modified: 11/3/22
"""

#***NEEDS WORK NOT DONE***

def euclidean_alg(a, b):
    #Get the larger of the two to set up the equivalence relation
    bigger = max(a,b)
    smaller = min(a,b)
    #Check if one of the two numbers is negative, but not both, if so than gcd = 1
    if((a < 0) != (b < 0)):
        print(f"Since {min(a,b)} is less than 0, GCD({a}, {b}) = 1")
    #If a or b is 0, then the gcd is the absolute value of the non zero number
    elif(a == 0):
        print(f"Since a = 0, GCD({a}, {b}) = {abs(b)}")
    elif(b == 0):
        print(f"Since b = 0, GCD({a}, {b}) = {abs(a)}")
    else:
        bigger = abs(bigger)
        smaller = abs(smaller)
        remainder = 1
        while(remainder != 0):
            quotient = bigger // smaller
            remainder = bigger % smaller
            print(f"{bigger} = {smaller} * {quotient} + {remainder}")
            if(remainder == 0):
                print(f"\nGCD({a}, {b}) = {smaller}")
            bigger = smaller
            smaller = remainder

euclidean_alg(1242124, 1242)