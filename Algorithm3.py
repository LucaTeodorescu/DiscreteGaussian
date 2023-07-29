# The following code is the python version of the Sampling Algorith of a Discrete Gaussian

import numpy as np
import math
from fractions import Fraction
import sample_bernoulli, sample_uniform

# Alg 1

def sample_bernoulli_exp(gamma):
    
    gamma_frac = Fraction(gamma)

    if gamma <= 1 and gamma >= 0:
        k = 1
        a = sample_bernoulli(gamma_frac/k)
        while a != 1:
            k += 1
            a = sample_bernoulli(gamma_frac/k)
            if a == 0:
                break
        if k % 2 == 0:
            return 1
        elif k % 2 == 1:
            return 0

    elif gamma > 1:
        gamma_counting = Fraction(gamma)
        for k in range(math.floor(gamma)):
            b = sample_bernoulli_exp(Fraction(1))
            gamma_counting = gamma_counting - 1
            if b == 0:
                return 0
        c = sample_bernoulli_exp(gamma_counting)
    
        


# Alg 2

def sample_geometric_exp(x):

    t = x.denominator

    u = sample_uniform(t)
    b = sample_bernoulli_exp(Fraction(u,t))

    while b !=1:
        u = sample_uniform(t)
        b = sample_bernoulli_exp(Fraction(u,t))
    
    v = 0
    a = Fraction(1,1)
    while sample_bernoulli_exp(a) != 1:
        v += 1
    value = v*t+u
    return value//x.numerator



def sample_discrete_laplace(lambd):

    lambda_frac = Fraction(lambd)

    while b !=1 or y != 0:

        b = sample_bernoulli(Fraction(1,2))
        y = sample_geometric_exp(1/lambda_frac)
    
    return y*(1 - 2*b)


# Alg 3

def floorsqrt(x):
    a = 0
    b = 1
    while b * b <= x:
        b = 2 * b
    while a + 1 < b:
        # this is a binary search
        c = (a + b)//2
        if c * c <= x:
            a = c
        else:
            b = c
    return a

def sample_discrete_gauss(sigma2):

    sigma2_frac = Fraction(sigma2)

    t = floorsqrt(sigma2)+1
    sample_y = sample_discrete_laplace(t)
    sample_c = ((abs(sample_y) - sigma2_frac/t)**2)/(2*sigma2_frac) 
    
    while sample_bernoulli_exp(sample_c) != 1:

        sample_y = sample_discrete_laplace(t)
        sample_c = ((abs(sample_y) - sigma2_frac/t)**2)/(2*sigma2_frac)
    return sample_y