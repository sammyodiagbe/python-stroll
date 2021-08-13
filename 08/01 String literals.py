# Learning how to manipulate strings in python

string = "That is Alice's cat"

# the backslash tells python this is not the closing single quote
string_with_escape_char = 'This is tobi\'s cat'

# placing an r before a string completely ignores escape characters
ignore_escape = r'escape characters are totally ignored \' \' '
multiple_line_str = '''
Our deepest fear is not that we are inadequate,
our deepest fear is that we are powerful beyond measure,
it is our light not our darkness, that frightens us
your playing small does not serve the world, there was nothing about
shrinking so that others can feel insecure around you,
we are all meant to shine as little children, and as we let our own light
shine we unconciously give others the permission to do the same.

'''
print(string)
print(string_with_escape_char)
print(ignore_escape)
print(multiple_line_str)