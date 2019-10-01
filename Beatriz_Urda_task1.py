#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plotting a graph containing the typical functions that describe the
computational cost of algorithms

Created on Fri Sep 27 17:23:55 2019

@author: beatrizurdag
"""

import matplotlib.pyplot as plt
import numpy as np
import math, scipy
import scipy.misc

# Defining x and y values
x = np.arange(0,101,1)

logf = np.log10(x)
power = np.exp2(x)
square = np.square(x)
fact = scipy.misc.factorial(x)
sqroot = np.sqrt(x)

# Plotting
plt.plot(x,fact, label="x!")
plt.plot(x,power, label="2^x")
plt.plot(x,square, label="x^2")
plt.plot(x,x, label="x")
plt.plot(x,sqroot, label="sqrt(x)")
plt.plot(x,logf, label="log(x)")
plt.ylim(0,1000)
plt.title("Computational cost functions")
plt.legend()
plt.show()



