n, x, y = map(int,input().split())
list1 = list(map(int,input().split()))
answer_1 = 0
answer_2 = 0
for i in range(n):
    answer_1 += list1[i] // x
    if((list1[i] // x ) * (y - x) < list1[i] % x):
        answer_2 += list1[i] % x - ((list1[i] // x ) * (y - x))
print(answer_1)
print(answer_2)