import re

phone_regex = r'\d\d\d-\d\d\d-\d\d\d\d'
print(phone_regex)
mo = re.findall(phone_regex, 'This is my number 123-123-1234')
print('Phone number found: ', mo)

advanced_regex_pattern = r'\+\d{1}-\d{3}-\d{3}-\d{4}'
result = re.findall(advanced_regex_pattern,
                    'Hey, give me a call at 8;46 on my cell no +1-555-222-2323')
print(result)
