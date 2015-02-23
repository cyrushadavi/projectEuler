__author__ = 'Cyrus'
from eulerUtils import primesfrom2to, sum_digits

primes = primesfrom2to(9999)
for i in xrange(10, len(primes)):
    if primes[i] >1000:
        break
nums = primes[i:]
