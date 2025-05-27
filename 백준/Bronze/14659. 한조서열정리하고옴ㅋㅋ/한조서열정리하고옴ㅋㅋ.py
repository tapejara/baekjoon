n = int(input())
h = list(map(int,input().split()))
answer = 0
temp = 0
a = 0
for i in range(n):
    if(a < h[i]):
        a = h[i]
        temp = 0
        continue
    temp += 1
    answer = max(temp,answer)
print(answer)