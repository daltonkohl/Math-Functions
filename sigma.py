"""
A program consisting of functions to calculate sigma of a number as well as 
the sum of sigmas of all divisors of a number.
Author: Dalton Kohl
Date Last Modified: 11/4/22
"""

def sigma(n):
    """
    Functions returns the sum of all positive divisors of n
    """
    sum = 0
    for i in range(n):
        #choosing i + 1 since we want all divisors of n starting from 1 to n, adding the divisor to sum
        if n % (i + 1) == 0:
            sum += i + 1
    return sum

def sum_sigma(n):
    """
    Function returns the sum of all the sigma values of all positive divisors of n
    """
    sum = 0
    for i in range(n):
        if n % (i + 1) == 0:
            sum += sigma(i+1)
    return sum


print(sum_sigma(10))
 