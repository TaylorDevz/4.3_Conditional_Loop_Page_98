# page 100 // homework 2021-01-07
# amended TASK: 
#               - progam that set total to 100
#               - and subtracts numbers 
#               - until user enters a number greater than 251
total = 100
number = 1 # define number with something that is not 'true' in while
count = 0 

# loop until the user enters a number greater than 251
# while number <= 251:
# while number < 252:
while not (number > 251):      # loop until 'number' is 'not' greater than '251'
    number = input("enter a number: ")
    number = int(number)
    total = total - number    
    count += 1      # short form of: '#count = count +1'
    print("count: ", count)
print(total) # print total after while loop
