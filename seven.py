"""
Project Euler No. 7
====================

10001st prime number.
"""

from math import ceil, sqrt

def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    max = int(ceil(sqrt(n + 1)))
    z = [2, 3] + [x for x in range(3, max, 2) if x % 3 != 0]
    for m in z:
        if (n % m) == 0:
            return False
    return True



count = 1
last_prime = None
start = 1
while count < 10001:
    if is_prime(start):
        count += 1
        last_prime = start
    start += 2

print last_prime