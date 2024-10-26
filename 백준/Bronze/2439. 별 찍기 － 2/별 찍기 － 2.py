a = int(input())
for i in range(a):
    b = ""
    for _ in range(a-i-1):
        b += " "
    for _ in range(i+1):
        b += "*"
    print(b)