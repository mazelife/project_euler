"""
Project Euler No. 9
====================

Find the sum of all the primes below two million.
"""

def naive_eratosthenes(maximum):
        D = {}
        q = 2
        while q < maximum:
            if q not in D:
                yield q
                D[q*q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p+q, []).append(p)
                del D[q]
            q += 1

print sum(naive_eratosthenes(2000000))