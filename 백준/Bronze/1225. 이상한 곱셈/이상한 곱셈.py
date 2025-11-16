a, b = input().split()
answer = 0
for i in range(len(a)):
    if(int(a[i]) == 0):
        continue
    for j in range(len(b)):
        answer += int(a[i]) * int(b[j])
print(answer)