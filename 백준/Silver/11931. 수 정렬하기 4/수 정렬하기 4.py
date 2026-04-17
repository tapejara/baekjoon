import sys
input = sys.stdin.readline
n = int(input())
list1 = [int(input()) for _ in range(n)]
list1.sort(reverse=True)
for num in list1:
    print(num)