#! python3

import math


def tempConversion(degrees, unit="C"):
    if unit == "C":
        converted = 9*(float(degrees)/5)+32
    elif unit == "F":
        converted = (5*(float(degrees)-32))/9
    return round(converted, 1)


def factorPair(number, factor):
    factors = number/factor
    answer =[int(factor), int(factors)]
    answer.sort()
    return answer
    
    


def cosineLaw():
    pass


def convertAngle():
    pass


def solution():
    pass


def quadratic():
    pass
