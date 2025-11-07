n = int(input())
for _ in range(n):
    t = int(input())
    answer = "YES"
    for i in range(2, 10**6 + 1):
        if(t % i == 0):
            answer = "NO"
    print(answer)