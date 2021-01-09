# progam that set total to 100
# and subtracts numbers until user enters a number greater than 251
total = 100
number = 1 # define number with something that is not 'true' in while
count = 0 
# loop until the user enters a number greater than 251
#while number < 252:
while count < 3:
    number = input("enter a number: ")
    number = int(number)
    total = total - number
    #count = count +1
    count += 1
    print("count: ", count)
print(total) # print total after while loop
