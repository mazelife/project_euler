"""
Project Euler No. 9
====================

A Pythagorean triplet is a set of three natural numbers, a < b < c, 
for which, a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def get_triple(m, n):
    assert m > n
    msqr = pow(m,2)
    nsqr = pow(n,2)
    a = msqr - nsqr
    b = 2 * m * n
    c = msqr + nsqr
    return (a,b,c)

def test_pairs(n):
    m = n + 1
    triple = (0,0,0)
    while sum(triple) <= 1000:
        triple = get_triple(m, n)
        yield triple
        m += 1

solution = None
start = 1
while not solution:
    s = [triple for triple in test_pairs(start) if sum(triple) == 1000]
    if len(s) == 1:
        print start
        solution = s[0]
    start += 1
a, b, c = solution

print a * b * c