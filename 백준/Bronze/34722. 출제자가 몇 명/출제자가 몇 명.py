n = int(input())
answer = 0
for _ in range(n):
    list1 = list(map(int,input().split()))
    if(list1[0] >= 1000 or list1[1] >= 1600 or list1[2] >= 1500 or 0 < list1[3] <= 30):
        answer += 1
print(answer)