my_dict = {'name': 'samson', 'favouriteGame': 'pubg', 'likes': 'soccer'}
print(my_dict)
print(my_dict['name'])
for value in my_dict:
    print(my_dict[value])


# key error exception
try:
    print(my_dict['somerandomlie'])
except KeyError:
    print("That key doesn't exist")