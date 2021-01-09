# page 100 // homework 2021-01-07
# buggy code as in page 100
# TASK:     find the bug using the debugger
total = 0
while number != 0:    # BUG: use of uninitialized variable 'number'
    number = input("enter a number: ")
    number = int(number)
    total = total + number
print(total)
