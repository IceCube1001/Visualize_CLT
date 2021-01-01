# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 07:52:16 2021

@author: Roy
"""
from numpy.random import seed
from numpy.random import randint
from numpy import mean
# seed the random number generator, so that the experiment is #replicable
seed(56)
# generate a sample of numbers
numbers = randint(0, 101, 500)
print(numbers)
print('The mean is {}'.format(mean(numbers)))