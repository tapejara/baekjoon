import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    name = input()
    clear = name.strip()
    print(clear.lower())