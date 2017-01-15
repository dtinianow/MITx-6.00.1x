'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:}
Number of vowels: 5
'''

def count_vowels(s):
    vowels = 0

    for letter in s:
        l = letter.lower()
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
            vowels += 1

    return "Number of vowels: " + str(vowels)
