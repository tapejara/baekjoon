n = int(input())
list1 = list(map(int,input().split()))
answer = [0] * n
for i in range(n):
    answer[i] = 1
    for j in range(i):
        if(list1[j] < list1[i]):
            answer[i] = max(answer[j] + 1, answer[i])
print(max(answer))