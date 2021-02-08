'''
create a program that guesses a secret number!
Using bisection search, the computer will guess the user's secret number!
'''

import math
import random
print("Please think of a number between 0 and 100!")

user_input = ''  # init blank input

message = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."

start = 0  # lower bound for binary sort
end = 100  # upper bound for binary sort
guessed_num = 50  # middle element

while user_input != 'c':
    print('Is your secret number {}?'.format(guessed_num))
    user_input = input(message)

    '''
    if predicted num is higher then serach in left side(smaller side) of list
    if predicted num is lower then serach in right side(greater side) of list
    '''
    #num is higher
    if user_input == 'h':
        end = guessed_num
        guessed_num = int((start + end)/2)

    # correct num
    elif user_input == 'l':
        start = guessed_num
        guessed_num = int((start + end)/2)

    # correct num
    elif user_input == 'c':
        print('Game over. Your secret number was: ', guessed_num)
        break

    # invalid input
    else:
        print('Sorry, I did not understand your input.')

-------------------------------------------------------------------------------------------------------------------------

# Write a Python function returns square


def square(x):
    return (x*x)


-------------------------------------------------------------------------------------------------------------------------

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic  a⋅x2+b⋅x+c .


def evalQuadratic(a, b, c, x):
    return(a*(x*x) + b*x + c)


-------------------------------------------------------------------------------------------------------------------------

# Write a Python function, fourthPower using square function


def fourthPower(x):
    return square(square(x))  # recursive call to function


-------------------------------------------------------------------------------------------------------------------------

# return true if num is odd (without using if)


def odd(x):
    n = x % 2
    while (n != 0):
        return True
        break

    while (n == 0):
        return False
        break


-------------------------------------------------------------------------------------------------------------------------
'''
Write an iterative function iterPower(base, exp) that calculates 
the exponential baseexp  by simply using successive multiplication.
'''


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result = result * base  # successive multi
        exp = exp - 1
    return result


'''
Write a function recurPower(base, exp) which 
computes base^exp  by recursively calling itself
'''


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if(exp > 0):
        exp = exp - 1
        return recurPower(base, exp) * base  # recursive call
    else:
        return 1


-------------------------------------------------------------------------------------------------------------------------
'''
The greatest common divisor of two positive integers is the 
largest integer that divides each of them without remainder
'''


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = 1
    for x in range(1, a):
        if(a % x == 0 and b % x == 0):


'''
Write a function gcdRecur(a, b) that implements this idea recursively.
Euclid formula
if a & b are positive int
if b = 0, then the answer is a
Otherwise, gcd(a, b) is the same as gcd(b, a % b)
keep dividing grater num by smaller num
'''


def gcdRecur(a, b):
    if a == 0:
        return b

    return gcdRecur(b % a, a)


-------------------------------------------------------------------------------------------------------------------------

# idea of bisection search to determine if a character is in a string
# implements the above idea recursively


def isIn(char, aStr):
    if(len(aStr) == 0):  # length of string is 0
        return False
    elif(char == aStr):  # length of string is 1
        return True

    mid = int(len(aStr)/2)  # middle of string

    if(mid == 0):
        if(char == aStr[0]):
            return True
        else:
            return False

    elif(aStr[mid] == char):  # if middle is qual to char
        return True
    else:
        if(char > aStr[mid]):  # search in right side of list if char is grater
            aStr = aStr[mid:]  # string slicing mid to end
            mid = int(len(aStr)/2)
        else:
            aStr = aStr[:mid]  # search in left side of list if char is small
            mid = int(len(aStr)/2)  # string slicing start to mid
        return isIn(char, aStr)


-------------------------------------------------------------------------------------------------------------------------

'''
function should sum the area and square of the perimeter of the regular
polygon.The function returns the sum, rounded to 4 decimal places.    
'''


def polysum(n, s):
    area = (0.25*n*(s*s)) / (math.tan(math.pi/n))  # formula for area
    perimeter = (n * s) * (n * s)  # perimeter square
    my_sum = area + perimeter
    return(round(my_sum, 4))  # print upto 4 decimal places
