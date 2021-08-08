# handling exceptions in our python programs would stop our program from crashing whenever there is an error


def divideBy(value_to_divide_by):
    try:
        return 40 / value_to_divide_by
    except ZeroDivisionError:
        print('Error: Invalid input')


print(divideBy(4))
print(divideBy(0))