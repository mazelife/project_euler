"""
Project Euler No. 5
====================

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
i = 2520
r = range(2, 21)
r.reverse()
while True: 
    solution = i
    for n in r:
        if i % n != 0:
            solution = False
            break
    if solution:
        print solution
        break
    else:
        i += 2