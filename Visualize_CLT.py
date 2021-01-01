# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 07:55:21 2021

@author: Roy
"""


from numpy.random import seed
from numpy.random import randint
from numpy import mean
import matplotlib.pyplot as plt
# seed the random number generator, so that the experiment is replicable
seed(56)
# calculate the mean 1000 times
means = [mean(randint(0, 101, 500)) for _i in range(1000)]
# plot the distribution of sample means
n, bins, patches = plt.hist(means, 30, density=True, facecolor='r', alpha=0.70)
plt.xlabel('Samples mean')
plt.ylabel('Probability')
plt.title('Visualize CLT')
plt.show()
print('The mean of the sample means is {}'.format(mean(means)))