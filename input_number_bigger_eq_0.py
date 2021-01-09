total = 0
number = 1 # define number with something that is not 'true' in while

# loop until the user enters a number smaller than 0
while number >= 0:    # check if number is 0 or greater
    number = input("enter a number: ")
    number = int(number)
    total = total + number
print(total) # print total after while loop
