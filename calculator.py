import math
def add(a, b):
    add = a + b
    return add

def sub(a, b):
    sub = a - b
    return sub

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