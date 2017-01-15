'''
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
'''

def count_bobs(s):
    bob_total = 0

    for i in range(len(s)):
        if s[i:i+3] == 'bob':
            bob_total += 1

    return "Number of times bob occurs is: " + str(bob_total)
