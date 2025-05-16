import sys
input = sys.stdin.readline
list1 = [0 for _ in range(1001)]
list1[0] = 1
list1[1] = 1
for i in range(2,1001):
    temp = 0
    for j in range(i, -1, -2):
        temp += list1[(i - j) // 2]
    list1[i] = temp
t = int(input())
for _ in range(t):
    print(list1[int(input())])