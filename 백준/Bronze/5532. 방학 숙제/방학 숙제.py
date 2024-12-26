l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = 0
f = 0
if(b % d >= 1):
    f += b // d + 1
else:
    f += b// d
if(a %  c >= 1):
     e += a // c + 1
else:
    e += a // c
if(e >= f):
    print(l - e)
else:
    print(l - f)