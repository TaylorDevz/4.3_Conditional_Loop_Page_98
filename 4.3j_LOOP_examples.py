# LEARN:
#
# https://www.w3schools.com/python/python_functions.asp
#   def
#
# https://www.w3schools.com/python/python_conditions.asp 
#   if, elif, else
#
# https://www.w3schools.com/python/python_while_loops.asp
#   while
#
# https://www.w3schools.com/python/python_for_loops.asp
#   for, range
#
# https://docs.python.org/3/tutorial/inputoutput.html
#   

print("Start program")

def function1():
    print("running code inside 'function1'")

def function_sqr(number):
    print("running code inside 'function_sqr'")
    res = number * number
    return res

stop_loop = 0
loop_counter = 0

############################################################ #1 while loop:
# print("=============================")
print("#1 WHILE loop start:")

while stop_loop == 0:
    loop_counter += 1
    print("entering while loop code, counter:", loop_counter)
    input_str = input("entering 'y': stops the loop  'b' breaks the loop  'f' call function1 <any number> to sqare that number: ")
    
    if input_str == 'y' or input_str == '':
        stop_loop = 1
        print('stopping the loop in the while condition')
    
    elif input_str == 'b':
        print("stopping the loop using the 'break' statement")
        break

    elif input_str == 'f':
        print("calling 'function1'")
        function1()

    elif input_str.isnumeric():
        number = int(input_str)
        result = function_sqr(number)
        print("result of function_sqr: ", result)

    else:
        print("your input string makes no sense")

print("#1 WHILE loop done")
print("=============================")

############################################################ #2 for range loop:
print("#2 FOR RANGE loop start:")

for i in range(3):
    print("value from 'range()': ", i)
    result = function_sqr(i)
    print("result of function_sqr(",i,"): ", result)

print("#2 FOR RANGE loop done")
print("=============================")

############################################################ #3 for array loop      of integers:

print("#3 FOR ARRARY loop start:")

some_array_with_integers = [9,8,7]
for i in some_array_with_integers:
    print("for value from array 'some_array_with_integers': ", i)
    result = function_sqr(i)
    print(f"result of function_sqr({i}): {result}")

print("#3 FOR ARRARY loop done")
print("=============================")

############################################################ #4 for array loop      of strings:

print("#4 FOR ARRARY loop of strings start:")

some_array_with_strings = ["bananas", "apples", "corn flakes"]
for s in some_array_with_strings:
    print(f"meschie likes to eat {s} ")

print("#3 FOR ARRARY loop done")
print("=============================")
