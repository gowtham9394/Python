""" Find the minimum of three values."""
num1 = int(input( "Enter first number: "))
num2 = int(input ("Enter second number: "))
num3 = int(input ("Enter third number: "))


minimum = num1

if num2 < minimum:
    minimum = num2

if num3 < minimum:
    minimum = num3

print('Minimum value is', minimum)