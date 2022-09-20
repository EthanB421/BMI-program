# Author: Ethan Bautista
# Project 1
# calculate sin taylor series by using for loop in python
import math
from math import *


def sinCalc(x):
    resultLong = 0
    iterations = 0
    for k in range(0,10,1):
        resultLong += (((-1)**k)/math.factorial((2*k)+1))*(x**((2*k)+1))
        iterations += 1
    result = round(resultLong,6)
    print("The result is:", result, "\nThis loop has iterated: ", iterations, " times")

while True:
    choice = int(input("Welcome to my program to calculate sin! \n1) pi/3\n 2)-pi/6 \n 3) 0.112 \n 4) pi\n 5)pi/2 \n 6)Option of your choice\n"))
    if (choice == 1):
        sinCalc(pi/3)
    elif (choice == 2):
        sinCalc(-pi/6)
    elif (choice == 3):
        sinCalc(0.112)
    elif (choice == 4):
        sinCalc(pi)
    elif (choice == 5):
        sinCalc(pi/2)
    elif (choice == 6):
        other = float(input("Please enter your desired x value: "))
        sinCalc(other)
    reset = int(input("Would you like to test another value? 1) Yes 2) No (input 1 or 2) "))
    if (reset==1):
        continue
    else:
        break
print("Thank you for using my program! ")

"""
Welcome to my program to calculate sin! 
1) pi/3
 2)-pi/6 
 3) 0.112 
 4) pi
 5)pi/2 
 6)Option of your choice
1
The result is: 0.866025 
This loop has iterated:  10  times
Would you like to test another value? 1) Yes 2) No (input 1 or 2) 1
Welcome to my program to calculate sin! 
1) pi/3
 2)-pi/6 
 3) 0.112 
 4) pi
 5)pi/2 
 6)Option of your choice
2
The result is: -0.5 
This loop has iterated:  10  times
Would you like to test another value? 1) Yes 2) No (input 1 or 2) 1
Welcome to my program to calculate sin! 
1) pi/3
 2)-pi/6 
 3) 0.112 
 4) pi
 5)pi/2 
 6)Option of your choice
3
The result is: 0.111766 
This loop has iterated:  10  times
Would you like to test another value? 1) Yes 2) No (input 1 or 2) 1
Welcome to my program to calculate sin! 
1) pi/3
 2)-pi/6 
 3) 0.112 
 4) pi
 5)pi/2 
 6)Option of your choice
4
The result is: -0.0 
This loop has iterated:  10  times
Would you like to test another value? 1) Yes 2) No (input 1 or 2) 1
Welcome to my program to calculate sin! 
1) pi/3
 2)-pi/6 
 3) 0.112 
 4) pi
 5)pi/2 
 6)Option of your choice
5
The result is: 1.0 
This loop has iterated:  10  times
Would you like to test another value? 1) Yes 2) No (input 1 or 2) 1
Welcome to my program to calculate sin! 
1) pi/3
 2)-pi/6 
 3) 0.112 
 4) pi
 5)pi/2 
 6)Option of your choice
6
Please enter your desired x value: 1.1543
The result is: 0.914512 
This loop has iterated:  10  times
Would you like to test another value? 1) Yes 2) No (input 1 or 2) 1
Welcome to my program to calculate sin! 
1) pi/3
 2)-pi/6 
 3) 0.112 
 4) pi
 5)pi/2 
 6)Option of your choice
6 
Please enter your desired x value: 2
The result is: 0.909297 
This loop has iterated:  10  times
Would you like to test another value? 1) Yes 2) No (input 1 or 2) 2
Thank you for using my program!
"""