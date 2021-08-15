import re

general_text = 'Hey, give me a call at 8;46 on my cell no +1-555-222-2323 1-555-222-2323'
phone_regex = r'\d\d\d-\d\d\d-\d\d\d\d'
print(phone_regex)
mo = re.findall(phone_regex, 'This is my number 123-123-1234')
print('Phone number found: ', mo)

advanced_regex_pattern = r'\+\d{1}-\d{3}-\d{3}-\d{4}'
result = re.findall(advanced_regex_pattern,
                    'Hey, give me a call at 8;46 on my cell no +1-555-222-2323 1-555-222-2323')
print(result)


#  optional matches
optional_regex = '\+?\d{1}-\d{3}-\d{3}-\d{4}'
optional_result = re.findall(optional_regex, general_text)
print(optional_result)

# matching ranges
ranges = '[0-9]{1,}'
ranges_matcher = re.findall(ranges, general_text)
print(ranges_matcher)

# groups regex
str_with_curse = 'Hey you motherfucker, - && 007james fuck youman, this is bullshit, you little shithole, donald trump always said nigeria is a shit hole'
regex_express = r'(?:fuck|FUCK|shit|shithole|bullshit)'
print(re.sub(regex_express, 'no-curse', str_with_curse))
# print(matches)

# start of string
regex = re.findall(r"(?:(?:fuck|mother|shit)fucker|f\S+)", str_with_curse)
print(regex)


# understanding groups
regex_list = ['guru99 get', "gurus99 give", "guru selenium"]

for element in regex_list:
    z = re.match(r"(g\w+)\W(g\w+)", element)
    if z:
        # this prints out the groups in the form of a tuple
        print(z.groups())
        # this actually prints our the match
        print(z.group())
