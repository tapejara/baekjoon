a = int(input())
for i in range(a):
    b = ""
    if(not a == 1):
        for _ in range(a-1-i):
            b += " "
    b += "*"
    for _ in range(i):
        b += "**"
    print(b)
for i in range(a-1):
    b = ""
    for _ in range(i+1):
        b += " "
    b += "*"
    for _ in range(a-2-i):
        b += "**"
    print(b)