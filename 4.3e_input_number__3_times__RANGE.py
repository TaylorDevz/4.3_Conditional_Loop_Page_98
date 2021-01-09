# page 100 // homework 2021-01-07
# amended TASK: 
#               - progam that set total to 100
#               - loop 3 times using 'range'
total = 100
count = 0 

# loop 3 times:
for x in range(3):   # range(3) means a set of number from 0-3 excl 3 i.e 0,1,2 
    number = input("enter a number: ")
    number = int(number)
    total -= number  # shorter form of 'total = total - number'    
    count += 1
    # print variables inside the loop: 
    print("count: ", count) 
    print("x: ", x) # the 'x' value fetched by 'for' from 'range()'

print("total:", total) # print total after while loop