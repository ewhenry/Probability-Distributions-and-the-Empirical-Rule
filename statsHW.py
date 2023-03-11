"""
Created on Fri Feb 17 2:19:15 2023

@author: Henry Wandover
"""

from math import sqrt


def mean(X:list):
    # Finds the mean of an inputed list, sum divded by size
    return sum(X) / len(X)

def variance(X:list):
    """Assumes that X is a list of numbers.
       Returns the variance of X.
       Put your code in here"""
    m = mean(X)
    sqr_X = []
    for i in X:
        sqr_X.append((i - m)**2)
    return sum(sqr_X) / (len(X) - 1)
    
def stdDev(X:list):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X
       Put your code in here """
    return sqrt(variance(X))