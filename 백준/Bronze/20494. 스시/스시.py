import sys
input = sys.stdin.readline
n = int(input())
list1 = [0 for _ in range(26)]
for i in range(n):
    a = input().strip()
    for j in range(len(a)):
        list1[ord(a[j]) - 65] += 1
print(sum(list1))