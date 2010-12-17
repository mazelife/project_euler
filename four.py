"""
Project Euler No. 4
====================

Find the largest palindrome made from the product of 2 three-digit numbers.

"""

def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

r = range(100,1000)
numbers = [(x * y) for x in r for y in r if x >= y]
print max(filter(is_palindrome, numbers))