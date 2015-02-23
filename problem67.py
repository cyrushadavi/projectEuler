import urllib2

f = urllib2.urlopen('https://projecteuler.net/project/resources/p067_triangle.txt')
response = f.read()
num = response.count('\n')
response = response.split('\n')
matrix = []
for i in xrange(0,len(response)-1):
    matrix.append(response[i].split(' '))
    for j in xrange(0,i+1):
        matrix[i][j] = int(matrix[i][j])
for i in xrange(len(matrix)-2,-1,-1):
    for j in xrange(0,len(matrix[i])):
        print max(matrix[i+1][j],matrix[i+1][j+1])
        matrix[i][j] = matrix[i][j] + max(matrix[i+1][j],matrix[i+1][j+1])
print matrix[0]