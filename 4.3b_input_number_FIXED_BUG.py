total = 0
number = 1 # bugfix: define the 'number' varible to a value that meets the condition of the loop below
           # nbb: the proposed solution of the book to duplicate functional code is a no go for pre-initializing variables (duplicate code -> increase of bugs)
while number != 0:    
    number = input("enter a number: ")
    number = int(number)
    total = total + number
print(total)
