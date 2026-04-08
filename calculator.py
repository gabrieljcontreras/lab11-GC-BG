"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError:
        print("Cannot have the square root of a negative number")
def hypotenuse(a,b):
    result = math.hypot(a,b)
    return result
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        result = b / a
        return result
    except ZeroDivisionError: # raise ZeroDivisionError if a == 0
        print("Division by zero not allowed")
def logarithm(a, b):
    try:
        result = math.log(a, b)
        return result
    except ValueError:
        print("Value Error")# use math library/raise ValueError

def exponent(a, b):
    return a**b



