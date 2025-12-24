n = int(input())
list1 = list(map(int,input().split()))
answer = 1
for i in range(1,n):
    if(list1[i - 1] >= list1[i]):
        answer = 0
print(answer)