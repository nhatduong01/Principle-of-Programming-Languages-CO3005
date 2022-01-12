#Write a Python function, whose name is area, which accepts the radius of a circle 
# as an input parameter and return the area
import math
def CircleArea (radius):
    return radius**2*math.pi
# print(CircleArea(1.1))
# Write a Python function check(lst,n) to test whether all numbers of the list lst is greater than the number n
def check(MyList, num):
    for i in MyList:
        if i <= num:
            return False
    return True
# Write a Python function gcd to return the greatest common divisor (GCD) of two positive integer parameters
def gcd(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
        return gcd(num1 - num2, num2)
    else:
        return gcd(num1, num2 - num1)
# Write a Python program which accepts a sequence of comma-separated numbers from user and
#  generate a list and a tuple with those numbers.
def ListAndTuple(myString):
    myList = []
    temp = ""
    for i in myString:
        if i != ',':
            temp += i
        else:
            myList.append((temp))
            temp =""
    myList.append((temp))
    return myList, tuple(myList)
print(ListAndTuple("1,  3,4,15,22,16,7"))


# Write a Python function product(lst) to return the product of the list lst of integers 
def product (myList):
    result = 1
    for i in myList:
        result*= i
    return result
# Write a Python function sum_of_cube(n) that takes a positive integer n and returns the sum of the cube of 
# all the positive integers smaller than n.

def sum_of_cube(n):
    result = 0
    for i in range(1,n):
        result += i**3
    return result
