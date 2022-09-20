#Author: Ethan Bautista
#Project 1
#BMI Calculator

            

def metric():
    while True:
        try:
            kg = float(input("Please input your weight in kg: "))
            meters = float(input("Please input your height in meters: "))
            metricResultLong = kg/meters
            metricResult = round(metricResultLong,2)
            print("Your BMI is: " + str(metricResult))
            if (metricResult < 18.5):
                print("You are underweight. Make sure to eat in a calorie surplus!")
                break
            elif (metricResult > 18.5) and (metricResult < 25):
                print("You are at a healthy weight. Keep up the good work!")
                break
            elif (metricResult > 25) and (metricResult < 30):
                print("You are overweight. Try eating in a slight calorie deficit.")
                break
            elif (metricResult > 30):
                print("You are OBESE! Your health is at serious risk! ")
                break
            print("Thank you for using my program!")
            break
        except ZeroDivisionError:
            print("Unable to divide by 0. Please enter a realistic number")
            continue
    print("Thank you for using my program!")

def usa():
    while True:
        try:
            lbs = int(input("Please enter your weight in pounds: "))
            feet = int(input("Please enter your height in inches: "))
            usaResultLong = 703 * (lbs/(feet**2))
            usaResult=round(usaResultLong,2)
            print( "Your BMI is: " + str(usaResult))
            if (usaResult < 18.5):
                print("You are underweight. Make sure to eat in a calorie surplus!")
                break
            elif (usaResult > 18.5) and (usaResult < 25):
                print("You are at a healthy weight. Keep up the good work!")
                break
            elif (usaResult > 25) and (usaResult < 30):
                print("You are overweight. Try eating in a slight calorie deficit.")
                break
            elif (usaResult > 30):
                print("You are OBESE! Your health is at serious risk! ")
                break
            print("Thank you for using my program!")
        except ZeroDivisionError:
            print("Unable to divide by 0. Please enter a realistic number")
            continue


def prompt():
    while True:
        try:
            choice = int(input("Would you like to use the metric or USA system? \n 1) Metric\n 2) USA System \n"))
            if (choice == 1):
                metric()
                break
            elif (choice ==2):
                usa()
                break
        except ValueError:
            print("Please input integer only...")
            continue
prompt()

""""
Test #1
Would you like to use the metric or USA system? 
 1) Metric
 2) USA System 
2
Please enter your weight in pounds: 150
Please enter your height in inches: 72
Your BMI is: 20.34
You are at a healthy weight. Keep up the good work!
"""

"""
Test Case #2
Would you like to use the metric or USA system? 
 1) Metric
 2) USA System 
2
Please enter your weight in pounds: 175
Please enter your height in inches: 68
Your BMI is: 26.61
You are overweight. Try eating in a slight calorie deficit.
"""
"""
Test Case #3
Would you like to use the metric or USA system? 
 1) Metric
 2) USA System 
1
Please input your weight in kg: 72
Please input your height in meters: 1.83
Your BMI is: 39.34
You are OBESE! Your health is at serious risk! 
Thank you for using my program!
"""

"""
Test case #4
Would you like to use the metric or USA system? 
 1) Metric
 2) USA System 
1
Please input your weight in kg: 50.5
Please input your height in meters: 1.68
Your BMI is: 30.06
You are OBESE! Your health is at serious risk! 
Thank you for using my program!
"""

"""
Abnormal Case: Inputting a string character instead of an integer
Would you like to use the metric or USA system? 
 1) Metric
 2) USA System 
f
Please input integer only...
Would you like to use the metric or USA system? 
 1) Metric
 2) USA System 
2
Please enter your weight in pounds: f
Please input integer only...
Would you like to use the metric or USA system? 
 1) Metric
 2) USA System 
2
Please enter your weight in pounds: 160
Please enter your height in inches: 67
Your BMI is: 25.06
You are overweight. Try eating in a slight calorie deficit.
"""

"""
Abnormal Case #2: Inputting 0 for height and weight.
Would you like to use the metric or USA system? 
 1) Metric
 2) USA System 
1
Please input your weight in kg: 0
Please input your height in meters: 0
Unable to divide by 0. Please enter a realistic number
Please input your weight in kg: 72
Please input your height in meters: 1.83
Your BMI is: 39.34
You are OBESE! Your health is at serious risk! 
Thank you for using my program!
"""
