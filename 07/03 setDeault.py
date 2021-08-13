# using setDefault to set the default value of a dictionary entry

new_dict = {'name': 'samson', 'best-color': 'blue', 'favourite-musician': 'Ed sheeran'}
new_dict.setdefault('favourtie-car', 'tesla')
# before changing the value of favourite car
print(new_dict)
new_dict['favourite-car'] = 'Maseratti'
 
#  after changing the value of favourite car
print(new_dict)