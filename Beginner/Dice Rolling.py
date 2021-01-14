import random
min = 1
max = 6
roll = 'yes'
 while roll == 'yes'or roll == 'y'
    print('rolling the dice')
    print('The values are......')
    print(random.randint(min, max))
    print(random.randint(min, max))

 roll = raw_input('roll the dice again')
