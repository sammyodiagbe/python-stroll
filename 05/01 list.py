import random as rand

# a list is a value that contains multiple values in an ordered sequence

my_list = [1,2,3,4,5]
print(type(my_list))
# accessing an item in the list is done using the square bracket with the index passed in between the brackets

#  should print out 3
print(my_list[2]) 
print(my_list)
# values can also be changed by using the index notation
my_list[3] = 5
print(my_list)

# looping through a list
for value in  my_list:
    print(value ** value)

another_list = list()

print(another_list)
another_list.append(20)

print(another_list)
another_list.append(40)
another_list.extend(my_list)
print(another_list)

another_list.insert(0, 55)


print(another_list)
new_list = []
for x in range(10):
    new_list.append(rand.randint(1,1000))

print(new_list)

# negative indexes can also be used to access
print(new_list[-1])
del new_list[-1]
print(new_list)

# checking if list contains a value
print(2 in my_list)
print(2 not in my_list)

another_value = ['osaro', 'ehis', 'oyakhilome']
samson, ehis, michael = another_value
print(samson)
print(ehis)
print(michael)

# sorting values in a list
another_list.sort()
print("After sorting another list")
print(another_list)