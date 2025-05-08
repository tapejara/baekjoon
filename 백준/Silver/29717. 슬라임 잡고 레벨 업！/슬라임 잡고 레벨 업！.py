import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    exp = (n ** 2 + n) // 2
    minimum, maximum = 1, 10 ** 9
    while minimum <= maximum:
        mid = (minimum + maximum) // 2
        temp = mid ** 2 + mid
        if(temp > exp):
            maximum = mid - 1
        else:
            minimum = mid + 1
    print(minimum)