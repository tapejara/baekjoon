n = int(input())
a, b, c = map(int,input().split())
answer = 0
if(n >= a):
    answer += a
else:
    answer += n
if(n >= b):
    answer += b
else:
    answer += n
if(n >= c):
    answer += c
else:
    answer += n
print(answer)