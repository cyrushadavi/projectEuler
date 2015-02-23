__author__ = 'Cyrus'

#DP solution for coin sums problem

target = 200
numbers = [1,2,5,10,20,50,100,200]
ways = [0 for i in xrange(0,target+1)]
ways[0] = 1
for n in numbers:
    for i in range(n,target+1):
        ways[i] += ways[i-n]
print ways[200]