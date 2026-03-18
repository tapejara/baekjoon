n = int(input())
list1 = [list(map(int,input().split())) for _ in range(n)]
sq = n * (n ** 2 + 1) // 2
check = set()
answer = "TRUE"
for i in range(n):
    for j in range(n):
        if(list1[i][j] in check):
            answer = "FALSE"
        else:
            check.add(list1[i][j])
for i in range(n):
    temp = 0
    for j in range(n):
        temp += list1[i][j]
    if(temp != sq):
        answer = "FALSE"
for i in range(n):
    temp = 0
    for j in range(n):
        temp += list1[j][i]
    if(temp != sq):
        answer = "FALSE"
temp1 = 0
for i in range(n):
    temp1 += list1[i][i]
if(temp1 != sq):
    answer = "FALSE"
temp2 = 0
for i in range(n):
    temp2 += list1[i][n - i - 1]
if(temp2 != sq):
    answer = "FALSE"
print(answer)