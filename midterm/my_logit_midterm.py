# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Midterm Examination: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for another script that would
# execute the scripts (to run the doctests)
# and imports the modules to test the functions.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module
from typing import List
import math
import numpy as np



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

def logit(x: float, b_0: float, b_1: float) -> float:
    """
    Computes the logit function.

    Parameters
    ----------
    x : float
        Independent variable.
    b_0 : float
        Intercept term.
    b_1 : float
        Coefficient of x.

    Returns
    -------
    float
        The computed logit probability.

    Examples
    --------
    >>> logit(1, 0, 1)
    0.7310585786
    >>> logit (2,0,2)
    0.9820
    >>> logit (3,0,3)
    0.9998    
    """
    exp_value = math.exp(b_0 + b_1 * x)
    return exp_value / (1 + exp_value)


def logit_like(yi: int, xi: float, b_0: float, b_1: float) -> float:
    """
    Computes the log-likelihood for logistic regression.

    Parameters
    ----------
    yi : int
        Dependent binary variable (0 or 1).
    xi : float
        Independent variable.
    b_0 : float
        Intercept term.
    b_1 : float
        Coefficient of xi.

    Returns
    -------
    float or None
        The log-likelihood value if yi is valid; otherwise, None.

    Examples
    --------
    >>> logit_like(1, 2, 0, 1)
    -0.126928011
    
    >>> logit_like(0, 2, 0, 1)
    -1.126928011
    
    >>> logit_like(2, 2, 0, 1)
    Warning: y is not binary. y should be either 1 or 0.
    None
    """
    p = logit(xi, b_0, b_1)
    
    if yi == 1:
        return math.log(p)
    elif yi == 0:
        return math.log(1 - p)
    else:
        print("Warning: y is not binary. y should be either 1 or 0.")
        return None
    
def logit_like_sum(y: list, x: list, beta_0: float, beta_1: float): #-> float
    """
    Compute the sum of the log-likelihood function for logistic regression.

    The logistic function is defined as:
        (x) = exp(beta_0 + x * beta_1) / (1 + exp(beta_0 + x * beta_1))

    The log-likelihood for each observation is:
        - If y_i = 1: log(ℓ(x; beta_0, beta_1))
        - If y_i = 0: log(1 - ℓ(x; beta_0, beta_1))

    Parameters:
    y (list of int): Binary outcome variable (0 or 1).
    x (list of float): Predictor variable.
    beta_0 (float): Intercept coefficient.
    beta_1 (float): Slope coefficient.

    Returns:
    float: Sum of log-likelihood values across all observations.

    Examples:
    >>> logit_like_sum([1, 0, 1], [2, -1, 0], 0.5, -0.25)
    -2.3040951708549517
    >>> logit_like_sum([0, 0, 1, 1], [3, -2, 1, 0], 0.2, 0.5)
    -3.2402116136010926
    >>> logit_like_sum([1, 1, 0, 0, 1], [1, 2, -1, -2, 0], -0.3, 0.4)
    -2.6633502627230934
    """
    if any(i not in {0, 1} for i in y):
        print("Error: all values in y list must be either 0 or 1")
        return None
    if len(x) != len(y):
        print("Error: lists x and y must have the same length")
        return None

    return sum(logit_like(y[i], x[i], beta_0, beta_1) for i in range(len(y)))







#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------


# Exercise 6


def max_logit(y: List[float], x: List[float], 
        beta_0_min: float, beta_0_max: float, 
        beta_1_min: float, beta_1_max: float, 
        step: float) -> float:
    """
    Calculates the estimated coefficients 
    by grid search on the value of the logit_like_sum function
    for the logistic regesssion model 
    given two lists of data y and x.
    
    The search is taken over a grid of candidate values
    of beta_0 and beta_1 defined over
    np.arange(beta_0_min, beta_0_max, step) and
    np.arange(beta_1_min, beta_1_max, step), respectively.
    
    
    >>> max_logit([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], \
                  -2.0, 2.0, -2.0, 2.0, 0.10)
    [0.0, 0.0]
    >>> max_logit([1, 0, 1], [15.0, 10.0, 5.0], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.69, 0.0]
    >>> max_logit([1, 0, 1, 0, 1], [0, 0, 1, 1, 1], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.0, 0.69]
    """
    
    beta_0_list = np.arange(beta_0_min, beta_0_max, step)
    beta_1_list = np.arange(beta_1_min, beta_1_max, step)
    
    max_logit_sum = float
    i_max = None
    j_max = None
    
    for i in range(len(beta_0_list)):
        for j in range(len(beta_1_list)):
            beta_0 = beta_0_list[i]
            beta_1 = beta_1_list[j]
            logit_sum_ij = logit_like_sum(y, x, beta_0, beta_1)
            if logit_sum_ij > max_logit_sum:
                max_logit_sum = logit_sum_ij
                i_max = i
                j_max = j

    if (i_max is not None and j_max is not None):
        return [beta_0_list[i_max], beta_1_list[j_max]]
    else:
        print("There was no value.")
        print("Different parameters needed for beta_0 and beta_1.")
    
    return None




# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# Make sure to include examples in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 







##################################################
# End
##################################################
