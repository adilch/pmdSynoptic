# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:54:50 2019

@author: adilj
"""

import numpy as np
import matplotlib.pyplot as plt

N = 10000

x = np.random.uniform(low=-1, high=1, size=[N,1])
y = np.random.uniform(low=-1, high=1, size=[N,1])

inside = x**2 + y**2 < 1

approxPi = 4 * np.sum(inside) / N

print ('Pi : {}, approxmation: {}'.format(np.pi, approxPi))

x_in = x[inside]
y_in = y[inside]

plt.figure(figsize=[5,5])
plt.scatter(x,y, s =2)
plt.scatter(x_in,y_in, color='r', s =2)
plt.show()