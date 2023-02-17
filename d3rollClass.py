# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 2:19 2023

@author: Henry Wandover
"""
import random
from math import sqrt
import pylab

vals = []

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

def roll():
    """Assumes numRolls a positive int"""
    return random.choice((1, 2, 3))

def rollSim(numTrials, numRollsPerTrial):
    ones, twos, threes = 0, 0, 0
    for i in range(numTrials):
        for i in range(numRollsPerTrial):
            r = roll()
            if r == 1:
                ones += 1
            elif r == 2:
                twos += 1
            else:
                threes += 1
    return (ones, twos, threes)

def labelPlot(numRolls, numTrials):
    pylab.title(str(numTrials) + ' trials of'
                + str(numRolls) + ' rolls each')
    pylab.xlabel('Results of a Roll')
    pylab.ylabel('Number of Trials')

def makePlot(num):
    pylab.bar(num, 200)

makePlot(rollSim(30,10))
