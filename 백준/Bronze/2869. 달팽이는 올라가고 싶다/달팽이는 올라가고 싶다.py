import math
a,b,c = map(int,input().split())
d = a - b
e = c -a
print(math.ceil(e / d) + 1)