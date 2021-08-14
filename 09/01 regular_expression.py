import re

phone_regex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
print(phone_regex)
mo = phone_regex.search('My number is 123-444-555-666')
print('Phone number found: ', mo)
