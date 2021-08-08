# this is a global variable
power = 200


def inside_func():
    inside_func_power = 10
    print(inside_func_power)

    # we can acess the power varible from inside this function because it is in a global scope
    print(power * inside_func_power)
inside_func()
# this should throw and error because inside_func_power is not accessible outside it parent function

# print(inside_func_power)