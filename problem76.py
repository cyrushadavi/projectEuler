__author__ = 'Cyrus'

target = 100
numbers = xrange(1,target)
ways = [0 for i in xrange(0,target+1)]
ways[0] = 1
for n in numbers:
    for i in range(n,target+1):
        ways[i] += ways[i-n]
print ways