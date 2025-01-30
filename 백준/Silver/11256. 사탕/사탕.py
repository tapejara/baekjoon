import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    j, n = map(int,input().split())
    box = []
    count = 0
    for i in range(n):
        r, c = map(int,input().split())
        box.append(r * c)
    while j > 0:
        j -= max(box)
        box.remove(max(box))
        count += 1
    print(count)