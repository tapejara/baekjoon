import sys
input = sys.stdin.readline
n, k = map(int,input().split())
pot = [int(input()) for _ in range(n)]
maximum, minimum = max(pot), 0
while minimum <= maximum:
    if(maximum + minimum == 0):
        break
    elif(maximum + minimum == 1):
        mid = minimum + maximum
    else:
        mid = (minimum + maximum) // 2
    count = 0
    for element in pot:
        count += element // mid
    if(count < k):
        maximum = mid - 1
    else:
        minimum = mid + 1
print(maximum)