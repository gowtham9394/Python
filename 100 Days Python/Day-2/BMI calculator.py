#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

#The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


##########################################################################################################################################################################################

#takes inputs from user
weight = input("Enter your weight in kg:\n")
height = input("Enter your height in meters: \n")

#converting weight and height type
int_weight = int(weight)
int_height = float(height)

#calcualte the BMI
BMI = int_weight / int_height ** 2

#converting the BMI into whole number
BMI_AS_INT = int(BMI)

#print the BMI
print("Your BMI is " + str(BMI_AS_INT))