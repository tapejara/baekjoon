import sys
input = sys.stdin.readline
n, m = map(int,input().split())
list_a = []
for _ in range(n):
    a = int(input())
    list_a.append(a)
list_a.sort()
set_a = set(list_a)
for _ in range(m):
    d = int(input())
    if(d in set_a):
        min, max = 0, n
        while min <= max:
            mid = (min + max) //2
            if( d <= list_a[mid]):
                max = mid - 1
            else:
                min = mid + 1
        print(min)
    else:
        print(-1)