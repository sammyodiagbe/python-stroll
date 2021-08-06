# control flows are how your python programs make decisions
# True or false variable types are known as Boolean values in programing

isTrue = False
if isTrue:
    print('The value is true')
else:
    print("The value is not true")


value1 = 15
value2 = 15

if value1 > value2: 
    print('Value one is heavier')
elif value1 == value2:
    print('Both values are the same')
else: 
    print('Value 2 is the larger of the variables')

# we can also have complex comparison for example

if (4 == 4) and (5 is not 5):
    print('That is one crazy comparison samson')
else: 
    print('Well i told you that is one crazy comparison, now see where we at')