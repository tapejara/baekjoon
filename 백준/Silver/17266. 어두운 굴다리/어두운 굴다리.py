from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
x = deque(map(int,input().split()))
if(not 0 in x):
    x.appendleft(0)
if(not n in x):
    x.append(n)
list1 = []
for i in range(len(x) - 1, 0, -1):
    if(x[i] == n or x[i] == x[1]):
        list1.append(x[i] - x[i - 1])
    else:
        list1.append((x[i] - x[i - 1]) / 2)
minimum, maximum = 0,n
while minimum <= maximum:
    mid = (minimum + maximum) // 2
    if(max(list1) > mid):
        minimum = mid + 1
    else:
        maximum = mid - 1
print(minimum)