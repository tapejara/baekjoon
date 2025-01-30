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
    box.sort(reverse = True)
    for i in range(n):
        if(j <= 0):
            break
        j -= box[i]
        count += 1
    print(count)