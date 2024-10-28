import sys
input = sys.stdin.readline
list = []
for i in range(9):
    a = int(input())
    list.append(a)
print(max(list),list.index(max(list))+1)