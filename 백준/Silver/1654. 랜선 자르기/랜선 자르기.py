import sys
input = sys.stdin.readline
k, n = map(int,input().split())
list1 = [int(input()) for _ in range(k)]
minimum, maximum = 0, 2**31 - 1
while minimum <= maximum:
    mid = (minimum + maximum) // 2
    temp = 0
    for i in range(k):
        temp += list1[i] // mid
    if(temp < n):
        maximum = mid - 1
    else:
        minimum = mid + 1
print(maximum)