'''
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters
occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print:
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
'''

def longest_alphabetic_substring(s):
    longest = current = ''

    for letter in s:
        if letter >= current[-1:]:
            current += letter
        else:
            current = letter

        if len(current) > len(longest):
            longest = current

    return "Longest substring in alphabetical order is: " + longest
