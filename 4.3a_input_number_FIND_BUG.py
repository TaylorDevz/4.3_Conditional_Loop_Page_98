total = 0
while number != 0:    # BUG: use of uninitialized variable 'number'
    number = input("enter a number: ")
    number = int(number)
    total = total + number
print(total)
