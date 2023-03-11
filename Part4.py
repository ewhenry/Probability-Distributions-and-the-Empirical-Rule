# -*- coding: utf-8 -*-
"""
@author: Henry Wandover
"""
from scipy.stats import norm
import numpy as np
import pylab

# Part 1
print(norm.pdf(0, 0, 1))
print(norm.pdf(0.5, 1, 3))

x = np.linspace(-4, 4)
y = norm.pdf(x, 1, 3)
pylab.figure(0)
pylab.plot(x,y)

# Part 2
print(norm.cdf(0, 0, 1))
print(norm.cdf(0.5, 1, 3))

y = norm.cdf(x, 1, 3)
pylab.figure(1)
pylab.plot(x,y)

# Part 3
print(norm.ppf(0.5, 1, 3))

y = norm.ppf(x, 1, 3)
pylab.figure(2)
pylab.plot(x,y)