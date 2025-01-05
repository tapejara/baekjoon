import sys
input = sys.stdin.readline
a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = 0
    e = 0
    for i in range(1,c + 1):
        if(b * i % c == 0):
            d += b * i
            break
    for i in range(min(b,c),0,-1):
        if(b % i == 0 and c % i == 0):
            e += i
            break
    print(d , e)
