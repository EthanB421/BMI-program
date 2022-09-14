#Author: Ethan Bautista
#Project 1
#BMI Calculator

def postScreen():
    while True:
        try:
            retry = int(input("Would you like to enter another BMI?\n 1) Yes \n 2) No\n"))
            if (retry==1):
                prompt()
            elif (retry==2):
                print("Thank you and gooodbye!")
                break
            else: 
                postScreen()
                break
        except ValueError:
            print("Please input integer only...")
            continue
            

def metric():
    kg = int(input("Please input your weight in kg: "))
    meters = float(input("Please input your height in meters: "))
    metricResultLong = kg/meters
    metricResult = round(metricResultLong,2)
    print("Your BMI is: " + str(metricResult))
    if (metricResult < 18.5):
        print("You are underweight. Make sure to eat in a calorie surplus!")
    elif (metricResult > 18.5) and (metricResult < 25):
        print("You are at a healthy weight. Keep up the good work!")
    elif (metricResult > 25) and (metricResult < 30):
        print("You are overweight. Try eating in a slight calroie deficit.")
    elif (metricResult > 30):
        print("You are OBESE! Your health is at serious risk! ")
    postScreen()

def usa():
    lbs = int(input("Please enter your weight in pounds: "))
    feet = int(input("Please enter your height in inches: "))
    usaResultLong = 703 * (lbs/(feet**2))
    usaResult=round(usaResultLong,2)
    print( "Your BMI is: " + str(usaResult))
    if (usaResult < 18.5):
        print("You are underweight. Make sure to eat in a calorie surplus!")
    elif (usaResult > 18.5) and (usaResult < 25):
        print("You are at a healthy weight. Keep up the good work!")
    elif (usaResult > 25) and (usaResult < 30):
        print("You are overweight. Try eating in a slight calroie deficit.")
    elif (usaResult > 30):
        print("You are OBESE! Your health is at serious risk! ")
    postScreen()

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


