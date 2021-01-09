# page 100 // homework 2021-01-07
# amended TASK: 
#               - progam that set total to 100
#               - loop 3 times
total = 100
count = 0 

# loop 3 times:
while count < 3:   
    number = input("enter a number: ")
    number = int(number)
    total -= number  # shorter form of 'total = total - number'
    
    count += 1  #shorter form of 'count = count +1'
    # print variables inside the loop: 
    print("count: ", count) 

print("total:", total) # print total after while loop