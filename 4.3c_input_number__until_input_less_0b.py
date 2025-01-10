# page 101 // homework 2021-01-07
# TASK 2: loop until the user enters a number smaller than 0
#
total = 0
number = 1 # define number with something that is not 'true' in while condition

# loop until the user enters a number smaller than 0
while not number < 0:    
    number = input("enter a number: ")
    number = int(number)
    total = total + number
print(total)
