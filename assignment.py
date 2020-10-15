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



def cosineLaw(side1, side2, angle, oppositeSide=True):
    import math
    x = toRadians(angle)
    if oppositeSide == True:
        answer1 = math.sqrt(side1**2 + side2**2 - 2*side1*side2*math.cos(x))
        return answer1
    elif oppositeSide == False:
        if side1 > side2:
            s = side2
        else:
            s = side1
        a = 1
        b = -2*s*math.cos(x)
        c = side2**2 - side1**2
        list1 = quadratic(a, b, c)
        answer2 = solution(list1)
        return answer2


def toRadians(angle):
    import math
    radianAngle = angle*(math.pi/180)
    x = float(radianAngle)
    return x


def quadratic(a, b, c):
    import math
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    answers = [x1, x2]
    answers.sort()
    return answers


def solution(a):
    y = a[1]
    return y







     