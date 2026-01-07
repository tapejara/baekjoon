import sys
input = sys.stdin.readline
t = int(input())
list1 = [0, 1]
for i in range(2, 1555):
    list1.append(list1[-1] + i)
for i in range(t):
    a, b = map(int,input().split())
    print(list1[a + b - 1] * (a + b))