import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    n -= 1
    count = 0
    minimum, maximum = 1, 4500
    while minimum <= maximum:
        mid = (minimum + maximum) // 2
        if(k * (mid ** 2 + mid) // 2 >= n):
            maximum = mid - 1
        else:
            minimum = mid + 1
    count = minimum
    distance = k * ((count ** 2 + count) // 2)
    if(count % 2 == 0):
        if(n == distance):
            print(-1 * k * count // 2, "R")
        else:
            print(-1 * k * count // 2 + (distance - n), "L")
    else:
        if(n == distance):
            print(k * (count // 2 + 1), "L")
        else:
            print(k * (count // 2 + 1) - (distance - n), "R")