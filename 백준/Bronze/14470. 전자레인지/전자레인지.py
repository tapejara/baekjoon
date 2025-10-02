a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
answer = 0
if(a < 0):
    answer += (0 - a) * c
    a = 0
if(a == 0):
    answer += d
if(a >= 0):
    answer += (b - a) * e
print(answer)