l, u = map(int,input().split())
answer = 0
mod = 10 ** 9 + 7
for i in range(l, u + 1):
    if(i < 3):
        answer += 1
    elif(i % 2 == 0):
        answer = (answer + pow(26, (i - 2) // 2, mod)) % mod
    else:
        answer = (answer + pow(26, (i - 2) // 2 + 1, mod)) % mod
answer %= mod
if(l != 2 and u != 1):
    print("A")
    print(answer)
else:
    print("H")
    print(answer)