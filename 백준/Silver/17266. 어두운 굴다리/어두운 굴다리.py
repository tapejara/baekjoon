import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
x = list(map(int,input().split()))
list1 = []
if(len(x) > 1):
    for i in range(len(x) - 1, 0, -1):
        list1.append((x[i] - x[i - 1]) / 2)
list1.append(n - x[-1])
list1.append(x[0] - 0)
minimum, maximum = 0,n
while minimum <= maximum:
    mid = (minimum + maximum) // 2
    if(max(list1) > mid):
        minimum = mid + 1
    else:
        maximum = mid - 1
print(minimum)