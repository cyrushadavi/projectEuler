__author__ = 'Cyrus'
from eulerUtils import primesfrom2to


num = 20
def findNumOfPrimeSums(target):
    numbers = primesfrom2to(target)
    ways = [0 for i in xrange(0,target+1)]
    ways[0] = 1
    for n in numbers:
        for i in range(n,target+1):
            ways[i] += ways[i-n]
    return max(ways)
while findNumOfPrimeSums(num) < 5000:
    num += 1

print num