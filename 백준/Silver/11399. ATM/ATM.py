import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
time = 0
total = 0
for i in range(n):
    time += list1[i]
    total += time
print(total)