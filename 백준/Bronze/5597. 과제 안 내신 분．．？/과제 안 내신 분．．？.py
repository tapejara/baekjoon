import sys
input = sys.stdin.readline
list = []
for _ in range(28):
    a = int(input())
    list.append(a)
b = 0
for i in range(1,31):
    if(list.count(i) == 0):
        print(i)