a, b = map(int,input().split(":"))
for i in range(2, min(a, b) + 1):
    if((a or b) < i):
        break
    while(a % i == 0 and b % i == 0):
        a //= i
        b //= i
print(f"{a}:{b}")