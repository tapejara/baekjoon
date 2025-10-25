origin = input()
n = int(input())
answer = 0
for _ in range(n):
    i = input()
    if(origin == i):
        answer += 1
print(answer)