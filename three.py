"""
Project Euler No. 2
====================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

LIMIT = 600851475143

def euler_sieve(n):
    candidates = range(n+1)
    end = (int(math.ceil(n**0.5)))
    for i in xrange(2, end +1):
          if not candidates[i]:
              continue
          candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]

last_value = None
for num in euler_sieve(int(math.ceil(LIMIT**0.5))):
    if LIMIT % num == 0:
        last_value = num
print last_value