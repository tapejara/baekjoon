import sys
input = sys.stdin.readline
a = int(input())
list = list(map(int, input().split()))
print(min(list), end=' ')
print(max(list))