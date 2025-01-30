import sys
input = sys.stdin.readline
n, k = map(int,input().split())
track = list(map(int,input().split()))
count = 0
for i in range(n - 1):
    if(track[i] >= track[i + 1] + k):
        print(-1)
        exit()
    elif(track[i] >= track[i + 1]):
        track[i + 1] += k
        count += 1
print(count)