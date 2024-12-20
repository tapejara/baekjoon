a = 0
for _ in range(5):
    b = int(input())
    if(b <= 40):
        a += 40
    else:
        a += b
print(a // 5)