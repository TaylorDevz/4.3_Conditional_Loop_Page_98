# progam that set total to 100
total = 100
number = 1 # define number with something that is not 'true' in while
count = 0 
# loop 3 times:


for x in range(3):   # range(3) means a set of number from 0-3 excl 3 i.e 0,1,2 
    number = input("enter a number: ")
    number = int(number)
    total = total - number
    #count = count +1
    count += 1
    print("count: ", count)
    print("x: ", x)
print(total) # print total after while loop
