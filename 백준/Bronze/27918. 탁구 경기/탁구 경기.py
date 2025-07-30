n = int(input())
x = 0
y = 0
for _ in range(n):
    a = input().strip()
    if(a == "D"):
        x += 1
    else:
        y += 1
    if(max(x, y) - min(x, y) >= 2):
        print(f"{x}:{y}")
        exit()
print(f"{x}:{y}")