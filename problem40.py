__author__ = 'Cyrus'


string = ''
for i in xrange(1,300000):
    string = string + str(i)

print int(string[0])* int(string[9])* int(string[99])* int(string[999])* int(string[9999])* int(string[99999])* int(string[999999])
