# the str(), len(), int(), float()
# they are used to convert other variable types to another varible type

value = 40
print(type(value))
change_value = float(value)
print(type(change_value))
convert_value_to_string = str(change_value)
print(type(convert_value_to_string))
print('notice how we constantly change value from an int to a float and then finally to a string')