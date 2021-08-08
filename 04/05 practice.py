def collatz(number):
    if number % 2:
        print(3 * number + 1)
        return 3 *  number + 1
    else:
        print( number // 2)
        return number // 2

def callCollatz():
    try:
        integer = int(input('Enter a number'))
        value = collatz(integer)
        while value != 1:
            callCollatz()
        return value
    except ValueError:
        print('Invalid input')


callCollatz()