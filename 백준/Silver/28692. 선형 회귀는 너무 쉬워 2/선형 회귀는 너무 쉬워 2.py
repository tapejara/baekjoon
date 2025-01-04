import sys
input = sys.stdin.readline
n = int(input())
totalX = 0
totalY = 0
totalXX = 0
totalXY = 0
for i in range(n):
    x, y= map(int,input().split())
    totalX += x
    totalY += y
    totalXX += x ** 2
    totalXY += x * y
if(n * totalXX - totalX ** 2 == 0):
    print("EZPZ")
else:
    a = (n * totalXY - totalX * totalY) / (n * totalXX - totalX ** 2 )
    b = (totalY - a * totalX) / n
    print(a , b)