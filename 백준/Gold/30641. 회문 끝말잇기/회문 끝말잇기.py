l, u = map(int,input().split())
answer = 0
mod = 10 ** 9 + 7
def function(a):
    a = bin(a)[3:]
    b = 26
    for i in range(len(a)):
        b = pow(b, 2, mod)
        if(a[i] == "1"):
            b = pow(b * 26, 1, mod)
    return b
for i in range(l, u + 1):
    if(i < 3):
        answer += 1
    elif(i % 2 == 0):
        answer += function(((i - 2) // 2)) % mod
    else:
        answer += function(((i - 2) // 2 + 1)) % mod
answer %= mod
if((l == 1 and u == 1) or l == 2):
    print("H")
    print(answer)
else:
    print("A")
    print(answer)