import sys
import heapq
input = sys.stdin.readline
n, m = map(int,input().split())
hqn = list(map(int,input().split()))
list1 = list(map(int,input().split()))
for i in range(n):
    hqn[i] *= -1
heapq.heapify(hqn)
flag = True
for i in range(m):
    a = -1 * heapq.heappop(hqn)
    if(a > list1[i]):
        heapq.heappush(hqn, list1[i] - a)
    elif(a < list1[i]):
        flag = False
        break
if(flag == True):
    print(1)
else:
    print(0)