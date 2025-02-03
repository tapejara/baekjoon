import sys
input = sys.stdin.readline
n, a, d = map(int,input().split())
list1 = list(map(int,input().split()))
count = 0
for i in range(n):
    if(list1[i] == a):
        count += 1
        a += d
print(count)