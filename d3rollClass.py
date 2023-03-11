# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 2:19:15 2023

@author: Henry Wandover
"""
from math import sqrt
import random
import pylab

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

def roll(numRolls):
    """Assumes numRolls a positive int"""
    ones, twos, threes = 0, 0, 0
    for i in range(numRolls):
        r = random.choice((1, 2, 3))
        if r == 1:
            ones += 1
        elif r == 2:
            twos += 1
        else:
            threes += 1
        
    return [ones, twos, threes]

def rollSim(numTrials, numRollsPerTrial):
    result = [0, 0, 0]
    for i in range(numTrials):
        rolled = roll(numRollsPerTrial)
        result[0] += rolled[0]
        result[1] += rolled[1]
        result[2] += rolled[2]
    return result

def rollMF(numRolls):
    """Assumes numRolls a positive int"""
    ones = 0
    for i in range(numRolls):
        if random.choice((1,2,3)) == 1:
            ones += 1
    return ones/float(numRolls)

def rollSimMF(numTrials, numRollsPerTrial):
    fracOnes = []
    for i in range(numTrials):
        fracOnes.append(rollMF(numRollsPerTrial))
    mean = sum(fracOnes) / len(fracOnes)
    sd = stdDev(fracOnes)
    return (fracOnes, mean, sd)

def rollTwoD3(numRolls):
    """Assumes numRolls a positive int"""
    rolledResults = [0, 0, 0, 0, 0]
    for i in range(numRolls):
        val1 = random.choice((1, 2, 3))
        val2 = random.choice((1, 2, 3))
        result = val1 + val2
        if (result == 2):
            rolledResults[0] += 1
        elif (result == 3):
            rolledResults[1] += 1
        elif (result == 4):
            rolledResults[2] += 1
        elif (result == 5):
            rolledResults[3] += 1
        elif (result == 6):
            rolledResults[4] += 1
    return rolledResults

def rollD6(numRolls):
    rolledResults = [0, 0, 0, 0, 0, 0]
    for i in range(numRolls):
        val = random.choice((1, 2, 3, 4, 5, 6))
        if (val == 1):
            rolledResults[0] += 1
        elif (val == 2):
            rolledResults[1] += 1
        elif (val == 3):
            rolledResults[2] += 1
        elif (val == 4):
            rolledResults[3] += 1
        elif (val == 5):
            rolledResults[4] += 1
        elif (val == 6):
            rolledResults[5] += 1
    return rolledResults


def makePlot(num, numRolls, numTrials):
    pylab.bar(1, num[0], 0.5, 0)
    pylab.bar(2, num[1], 0.5, 0)
    pylab.bar(3, num[2], 0.5, 0)
    pylab.title(str(numTrials) + ' trials of '
                + str(numRolls) + ' rolls each')
    pylab.xlabel('Results of a Roll')
    pylab.ylabel('Number of Trials')

def makePlot(num, numTrials):
    pylab.bar(2, num[0])
    pylab.bar(3, num[1])
    pylab.bar(4, num[2])
    pylab.bar(5, num[3])
    pylab.bar(6, num[4])
    pylab.title(str(numTrials) + ' trials of adding two D3')
    pylab.xlabel('Results of a Roll')
    pylab.ylabel('Number of Trials')

def makePlotD6(num, numTrials):
    pylab.bar(1, num[0])
    pylab.bar(2, num[1])
    pylab.bar(3, num[2])
    pylab.bar(4, num[3])
    pylab.bar(5, num[4])
    pylab.bar(6, num[5])
    pylab.title(str(numTrials) + ' trials of Rolling a D6')
    pylab.xlabel('Results of a Roll')
    pylab.ylabel('Number of Trials')

def showErrorBars(minExp, maxExp, numTrials):
    """Assumes minExp and maxExp positive ints; minExp < maxExp
         numTrials a positive integer
       Plots mean fraction of heads with error bars"""
    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp + 1):
        xVals.append(2**exp)
        fracOnes, mean, sd = rollSimMF(2**exp, numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.errorbar(xVals, means, yerr=1.96*pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Ones ('
                + str(numTrials) + ' trials)')
    pylab.xlabel('Number of rolls per trial')
    pylab.ylabel('Fraction of Ones & 95% confidence')

    
#makePlot(rollSim(30,10), 30, 10)

#makePlot(rollSim(3000,10), 3000, 10)

#showErrorBars(3, 12, 3000)

#makePlot(rollTwoD3(60), 60)

#makePlot(rollTwoD3(6000), 6000)

makePlotD6(rollD6(6000), 6000)
