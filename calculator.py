import math
def add(a, b):
    add = a + b
    return add


# First example
import math
def square_root(a):
    if a < 0:
        raise ValueError("Cannot have the square root of a negative number")
    return math.sqrt(a)
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
    if a <= 0:
        raise ValueError("Value Error")
    return math.log(a, b)

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