#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x days, y weeks, and z months left.

#Where x, y and z are replaced with the actual calculated numbers.

age = input( "Enter your current age \n")

years = 90 - int(age)

months = round(years * 12)
weeks = round(years * 52)
days = round(years *365)

print(f"You have {days}, {weeks} weeks and {months} months left.")

