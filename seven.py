"""
Project Euler No. 7
====================

10001st prime number.
"""

from math import ceil, sqrt

def is_prime(n):
    if n in [2,3]:
        return True
    max = int(ceil(sqrt(n + 1)))
    z = [x for x in range(3, max, 2) if x % 3 != 0]
    z.insert(0, 2)
    z.insert(0, 3)
    for m in z:
        if (n % m) == 0:
            return False
    return True



count = 2
start = 3
while count < 10001:
    if is_prime(start):
        count += 1
    start += 2

print start