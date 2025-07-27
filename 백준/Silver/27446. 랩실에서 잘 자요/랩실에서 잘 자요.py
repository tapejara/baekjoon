n, m = map(int,input().split())
set1 = set(map(int,input().split()))
list1 = []
for i in range(1, n + 1):
    if(i not in set1):
        list1.append(i)
pg = 0
answer = 0
for i in range(len(list1)):
    if(answer == 0):
        answer += 7
    elif(2 * (list1[i] - pg) > 7):
        answer += 7
    elif(2 * (list1[i] - pg) <= 7):
        answer += 2 * (list1[i] - pg)
    pg = list1[i]
print(answer)