import sys
input = sys.stdin.readline
list1 = [0, 1, 2]
count = 1
for i in range(3, 10001):
    if(i % 6 == 1):
        list1.append(list1[-1] + (i // 6))
    else:
        list1.append(list1[-1] + (i // 6) + 1)    
t = int(input())
for i in range(t):
    print(list1[int(input())])