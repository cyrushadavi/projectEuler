__author__ = 'Cyrus'
def grid_dp(n):
    DPTable = [[0 for i in xrange(0,n)] for i in xrange(0,n)]
    for i in xrange(0, n):
        DPTable[i][0] = 1
        DPTable[0][i] = 1
    for i in xrange(1,n):
        for j in xrange(1,n):
            DPTable [i][j] = DPTable[i][j-1] + DPTable[i-1][j]
    #print DPTable
    return DPTable[n-1][n-1]

def grid(n):
    return gridhelper(n, n)

print grid_dp(21)