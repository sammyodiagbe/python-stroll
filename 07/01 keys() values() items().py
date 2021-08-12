dictionary = {'one': 1, 'two': 2, 'three' : 3, 'four' : 4, 'five' : 5};

# looping through dictionary key
for key in dictionary.keys():
    print(key)

# loopinf through dictionary items:
for value in dictionary.values():
    print(value)

# looping over items , this returns a tuple for each entry

for val in dictionary.items():
    print(type(val))