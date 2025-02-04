import sys
input = sys.stdin.readline
n = int(input())
list_a = list(map(int,input().split()))
a1 = list_a.pop(0)
list_a.sort()
for i in range(len(list_a)):
    if(list_a[i] < a1):
        a1 += list_a[i]
    else:
        print("No")
        exit()
print("Yes")