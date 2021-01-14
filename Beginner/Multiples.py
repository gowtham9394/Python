"""Use if statements to determine whether 1024 is a multiple of 4 and
whether 2 is a multiple of 10.
"""

num = 1024
mod = num % 4
if mod > 0:
    print ("1024 is not muitple of 4")
else:
    print("1024 is a muitple of 4")

num = 10
mod = num % 2
if mod > 0:
    print("10 is not muitple of 2")
else:
    print("10 is a muitple of 2")

