__author__ = 'Cyrus'

def countNumOfWays(tileLen, rowLen):
    table = [[0 for i in xrange(rowLen+1)] for i in xrange(rowLen+1)]
    count = 1
    for i in xrange(tileLen,rowLen+1):
        table[i][0] = count
        count+=1
    for j in xrange(tileLen*2,rowLen+1):
        for i in xrange(1,rowLen+1):
            table[j][i] = table[j-tileLen]
    print table
countNumOfWays(2,10)