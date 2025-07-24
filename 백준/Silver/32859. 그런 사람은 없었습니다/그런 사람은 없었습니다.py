import sys
input = sys.stdin.readline
n, m = map(int,input().split())
s = int(input())
list1 = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int,input().split())
    if(b == 0):
        for i in range(n + 1):
            if(list1[i] >= 1):
                list1[i] += 1
    if(b == 1 and list1[a] == 0):
        list1[a] = 1
    elif(b == 0 and list1[a] <= s + 1):
        list1[a] = -1
temp = False
for i in range(n + 1):
    if(list1[i] > s):
        temp = True
        print(i)
if(temp == False):
    print(-1)