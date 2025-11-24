n, m = map(int,input().split())
point = list(map(int,input().split()))
total_point = [0 for _ in range(m)]
tester = []
for i in range(m):
    temp = list(input().split())
    tester.append(int(temp[0]))
    for j in range(n):
        if(temp[j + 1] == "O"):
            total_point[i] += point[j]
answer_tester = []
for i in range(m):
    if(total_point[i] == max(total_point)):
        answer_tester.append(tester[i])
print(min(answer_tester), max(total_point))