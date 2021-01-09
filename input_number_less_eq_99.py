# progam that set total to 100
# and subtracts numbers until user enters a number greater than 99
total = 100
number = 1 # define number with something that is not 'true' in while

# loop until the user enters a number greater than 99
while number < 100:
    number = input("enter a number: ")
    number = int(number)
    total = total - number
print(total) # print total after while loop
