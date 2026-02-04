import sys
input = sys.stdin.readline
n, m =map(int,input().split())
list1 = list(map(int,input().split()))
minimum, maximum = 0,max(list1)
while minimum <= maximum:
    mid = (minimum + maximum) // 2
    temp = sum([ element - mid for element in list1 if element > mid ])
    if(temp < m):
        maximum = mid - 1
    else:
        minimum = mid + 1
print(maximum)