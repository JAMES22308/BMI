import math      # library for arithmetic sequence
import pyttsx3   # library for talking artificial intelligence

jarvis = pyttsx3.init()   #Initialization for the name of AI
rate = -5000              # rate is for talking speed
jarvis.setProperty('rate', rate)
name = input("name: ")          # Get the user's name
height = float(input("Enter your height in cm: "))  # Get the height of the user
weight = float(input("Enter your weight in kg: "))  # Get the weight of the user

bmi = weight / (height/100)**2     # Just simply divide the height to 100 and to the power of 2
print(f"Your BMI  is {bmi}")    # Print it 

# if and else statement
if bmi <= 18.4: # if the bmi is less than or equal to 18.4, it's underweight
    print(f"underweight.{name}")
elif bmi <= 24.9:   # if the bmi is less than or equal to 24.9, it's healthy
    print(" AI IS TALKING... ")
    jarvis.say(f" HELLO BOSS {name}, I AM JARVIS, BASED ON THE CALCULATION ON THE PROGRAM, YOUR BMI IS HEALTHY")
elif bmi <= 29.9:   # if the bmi is less than or equal to 29.9, it's over weight
    print(f"You are over weight. {name}")
    jarvis.say(f"You are over weight {name}")
elif bmi <= 34.9:   # if the bmi is less than or equal to 34.9, it's severely overweight
    print(f"You are severely over weight. {name}")
    jarvis.say(f" You are severely over weight {name}")
    
elif bmi <= 39.9:   # if the bmi is less than or equal to 39.9, it's obese
    print(f"You are obese.{name}")
    jarvis.say(f"You are obese {name}")
else:
    print(f" you're literally unhealthy, obese.{name}")
jarvis.runAndWait()