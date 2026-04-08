import math
def add(a, b):
    add = a + b
    return add


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

def logarithm(a, b):
    try:
        result = math.log(a, b)
        return result
    except ValueError:
        print("Value Error")# use math library/raise ValueError

def exponent(a, b):
    return a**b


def mul(a, b):
    mul = a * b
    return mul

def div(a, b):
    try:
        div = a / b
        return div
    except ZeroDivisionError:
        print("Error: cannot divide by zero")

def log(a, b):
    try:
        logarithm = log(a,b)
        return logarithm
    except ValueError:
        print("Error: value error")

def exp(a, b):
    exp = a**b
    return exp