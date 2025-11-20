import math
a, b, n, k = map(int,input().split())
i = math.ceil(math.ceil(k / n) / b)
if(k % (b * n) == 0):
    j = b
else:
    j = math.ceil((k % (b * n)) / n)
print(i, j)