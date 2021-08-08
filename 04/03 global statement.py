def spam():
    global eggs
    eggs = 'spam'


eggs = 'some random stuff'
print('first line, ', eggs)
spam()
print(eggs)