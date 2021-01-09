# page 101 // homework 2021-01-07
# TASK 3: 
#           - write a progam that set the 'total' variable to 100
#           - and subtracts input numbers from the 'total' variable 
#           - until user enters a number greater than 99
#
total = 100
number = 1 # define number with something that is not 'true' in while

# loop until the user enters a number greater than 99 (i.e. 100 or greater)
while number <= 99:  # same as:      'while number < 100:'
    number = input("enter a number: ")
    number = int(number)
    total = total - number
print(total) # print total after while loop
