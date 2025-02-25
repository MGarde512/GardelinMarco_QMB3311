# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Marco Gardelin
#
# Date: 02/25/2025
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
import math
import doctest
##################################################

# import name_of_module

import numpy as np


##################################################
# Function Definitions
##################################################


# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------
def CESutility(x: float, y: float, r: float) -> float:
    """
    Calculates the Constant Elasticity of Substitution (CES) utility function.

    Parameters
    ----------
    x : float
        Quantity of good 1.
    y : float
        Quantity of good 2.
    r : float
        Parameter that represents the degree to which the goods are complements or substitutes.

    Returns
    -------
    CESutility : float
        The computed CES utility value, or None if invalid input is detected.

    Examples
    --------
    >>> CESutility(5, 4, 7)
    8.515577021

    >>> CESutility(2, 5, 10)
    5.962990247

    >>> CESutility(8, 2, 3)
    8.513313739
    """
    if x < 0 or y < 0 or r <= 0:
        print("Warning: Invalid input detected. Returning None.")
        return None

    return (x ** r + y ** r) ** (1 / r)

def CESutility_valid(x: float, y: float, r: float) -> float:
    """
    Validates the input values and computes the CES utility function.

    Parameters
    ----------
    x : float
        Quantity of good 1.
    y : float
        Quantity of good 2.
    r : float
        CES utility parameter, must be strictly positive.

    Returns
    -------
    float or None
        The CES utility value if inputs are valid; otherwise, None.

    Examples
    --------
    >>> CESutility_valid(5, 4, 7)
    8.515577021
    
    >>> CESutility_valid(-1, 2, 3)
    Error: x must be a non-negative number
    None
    """
    if x >= 0 and y >= 0 and r > 0:
        return CESutility(x, y, r)
    
    if x < 0:
        print("Error: x must be a non-negative number")
    if y < 0:
        print("Error: y must be a non-negative number")
    if r <= 0:
        print("Error: r must be a strictly positive number")
    
    return None

def CESutility_in_budget(x: float, y: float, r: float, p_x: float, p_y: float, w: float) -> float:
    """
    Computes the CES utility if the budget constraint is met.

    Parameters
    ----------
    x : float
        Quantity of good 1.
    y : float
        Quantity of good 2.
    r : float
        CES utility parameter, must be strictly positive.
    p_x : float
        Price of good 1.
    p_y : float
        Price of good 2.
    w : float
        Total budget.

    Returns
    -------
    float or None
        The CES utility value if the budget constraint is satisfied; otherwise, None.

    Examples
    --------
    >>> CESutility_in_budget(5, 4, 7, 2, 3, 50)
    8.515577021
    
    >>> CESutility_in_budget(5, 4, 7, 2, 3, 10)
    None
    """
    if w < (p_x * x + p_y * y) or p_x < 0 or p_y < 0 or w < 0:
        return None
    return CESutility_valid(x, y, r)

def total_revenue(num_units: float, unit_price: float) -> float:
    """
    Calculates total revenue from selling a product at a fixed price.

    Parameters
    ----------
    num_units : float
        Number of units sold.
    unit_price : float
        Price per unit in dollars.

    Returns
    -------
    total_revenue : float
        The total revenue earned, or None if invalid input is detected.

    Examples
    --------
    >>> total_revenue(1000, 1000)
    1000000

    >>> total_revenue(2000, 2000)
    4000000

    >>> total_revenue(500, 456)
    228000
    """
    if num_units < 0 or unit_price < 0:
        print("Invalid input: Negative values are not allowed.")
        return None

    return num_units * unit_price


def total_cost(num_units: float, multiplier: float, fixed_costs: float) -> float:
    """
    Calculates the total cost to produce a product.

    Parameters
    ----------
    num_units : float
        Number of units produced.
    multiplier : float
        A constant multiplied by the square of the number of units produced.
    fixed_costs : float
        Fixed costs in dollars.

    Returns
    -------
    total_cost : float
        The total cost incurred, or None if invalid input is detected.

    Examples
    --------
    >>> total_cost(100, 50, 100)
    50100

    >>> total_cost(200, 100, 70)
    40070

    >>> total_cost(70, 120, 50)
    58850
    """
    if num_units < 0 or multiplier < 0 or fixed_costs < 0:
        print("Invalid input: Negative values detected. Returning None.")
        return None

    return multiplier * (num_units ** 2) + fixed_costs



#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 1
def total_profit(num_units:float, unit_price:float, 
                 multiplier:float, fixed_cost:float) -> float:
    """
    Calculates the total profit.
    
    
    Parameters
    ----------
    num_units : float
        Number of units produced.
    unit_price : float
            Price per unit in dollars.
    multiplier : float
        A constant multiplied by the square of the number of units produced.
    fixed_costs : float
        Fixed costs in dollars.
    
        
    
    Returns
    -------
    totoal_profit : float 
        Returns the total profit 
    
        
    Examples
    --------
    
    >>> total_profit(37, 264, 32, 45)
    -34085
    >>> total_profit(10, 300, 14, 60)
    1540
    >>> total_profit(30, 6000, 20, 80)
    161920
    """
    
    revenue = total_revenue(num_units, unit_price)
    cost = total_cost(num_units, multiplier, fixed_cost)
    profit = revenue - cost
    
    return profit


# Exercise 2

def max_profit_calc(unit_price: float, multiplier: float, fixed_cost: float) -> float:
        """
        Calculates the quantity to produce that maximizes profit.
        
        Parameters
        ----------
        unit_price : float
            Price per unit in dollars.
        multiplier : float
            A constant multiplied by the square of the number of units produced.
        fixed_costs : float
            Fixed costs in dollars.
        
            
        Returns
        -------
        q star : float
            The max profit
        
        
        >>> max_profit_calc(90, 0.6, 3)
        500.0
        >>> max_profit_calc(100, 3, 1)
        16.666
        >>> max_profit_calc(1, 1, 5)
        0
        """
        
        q_star = unit_price/(2*multiplier)
        profit = total_profit(q_star, unit_price, multiplier, fixed_cost)
        if profit < 0:
            q_star = 0
            
        return q_star



# Exercise 3

def profit_max_q(q_max:float, step:float, unit_price:float, 
                 multiplier:float, fixed_cost:float) -> float:
    """
    Calculates the quantity to produce that maximizes profit.
    
    Parameters
    ----------
    
    q_max : float
    step : float
    unit_price : float
    mulitiplier : float
    fixed_cost : float
    
    
    Returns
    -------
    q_listmax : float
        
    
    
    Exampeles
    ---------
    
    >>> profit_max_q(2000, 34, 1000, 0.10, 4)
    1972
    >>> profit_max_q(100000, 1, 20, 2.5, 10)
    4
    >>> profit_max_q(10000, 1, 20, 2.5, 5000)
    0
    """
    
    q_list = np.arange(0, q_max, step) 
    i_max = 0
    max_profit = 0
    for i in range(len(q_list)):
        q_i = q_list[i]
        profit_i = total_profit(q_i, unit_price, multiplier, fixed_cost)
        if (profit_i > max_profit):
            i_max = i
            max_profit = profit_i
            
    if (max_profit < 0):
        print("Not a positive value.")
        return 0
    else:
        return q_list[i_max]
        





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
