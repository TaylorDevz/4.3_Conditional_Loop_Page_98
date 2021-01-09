# page 100 // homework 2021-01-07
# add input 'number' to 'total' variable until user enter 0
# proof:  'for' loop can be used for conditional loops
#
total = 0
# define function behaving the same as 'range(inf)', but return only 0 values
def infinity_0():
    index = 0
    while True:
        yield index

for i_always_0 in infinity_0():
    print ('debug print: i_always_0=',i_always_0)
    number = int(input("enter a number: "))
    total += number
    if number == 0:
        break
print(total)
