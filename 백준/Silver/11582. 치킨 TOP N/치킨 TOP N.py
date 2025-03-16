import sys
input = sys.stdin.readline
n = int(input())
chicken = list(map(int,input().split()))
k = int(input())
def function(x, y, list1):
    if(y == 1):
        list1.sort()
        return list1
    else:
        return function(x // 2, y // 2, list1[:x // 2]) + function(x // 2, y // 2, list1[x // 2:])
for element in function(n, k, chicken):
    print(element, end=" ")