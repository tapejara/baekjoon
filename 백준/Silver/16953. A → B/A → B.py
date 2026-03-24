a, b = map(int,input().split())
if(a == b):
    print(0)
    exit()
answer = 1
while b > a:
    if(b % 2 == 0):
        b //= 2
        answer += 1
    elif(str(b)[-1] == "1"):
        b -= 1
        b //= 10
        answer += 1
    else:
        break
if(b == a):
    print(answer)
else:
    print(-1)