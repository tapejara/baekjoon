import sys
input = sys.stdin.readline
n, k = map(int,input().split())
list1 = []
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(k):
        list1.append((temp[j], i + 1))
x = list1[0][0]
point = 0
while len(list1) > 1:
    del list1[point]
    
    b = (point + x - 1) % len(list1)
    x = list1[b][0]
    point = b
    
print(list1[0][1], list1[0][0])