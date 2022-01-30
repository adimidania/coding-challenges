'''
input : a string
output : a boolean value
Keep in mind we need to transform all the letters to lowercase and keep only letters [a-z]
meaning, we have to remove all the whitespaces, numbers and special chars
'''

# Using regex
import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards