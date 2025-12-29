list0 = list(map(int,input().split()))
n = int(input())
answer = 0
for i in range(n):
    a, b, c = map(float,input().split())
    if(b >= 2.0 and c >= 17):
        answer += list0[int(a)]
print(answer)