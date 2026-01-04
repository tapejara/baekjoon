m = int(input())
n = int(input())
list1 = [i ** 2 for i in range(101)]
answer = []
for i in range(101):
    if(m <= list1[i] and list1[i] <= n):
        answer.append(list1[i])
if(answer):
    print(sum(answer))
    print(min(answer))
else:
    print(-1)