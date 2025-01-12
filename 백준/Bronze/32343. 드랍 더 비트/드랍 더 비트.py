n = int(input())
a, b = map(int,input().split())
listX = []
listY = []
listB = []
answer = []
for i in range(2 ** n):
    x = ""
    y = ""
    while True:
        if(i > 1):
            x += str(i % 2)
            y += str(i % 2)
            i //= 2
        else:
            x += str(i % 2)
            y += str(i % 2)
            break
    if(len(x) < n):
        x += "0" * (n - len(x))
    if(len(y) < n):
        y += "0" * (n - len(y))
    if(x.count("1") == a):
        listX.append(x[::-1])
    if(y.count("1") == b):
        listY.append(y[::-1])
for elemntX in listX:
    if(len(elemntX) != n):
        continue
    for elementY in listY:
        binary = ""
        if(len(elementY) != n):
            continue
        for i in range(n):
            if(elemntX[i] == elementY[i]):
                binary += "0"
            else:
                binary += "1"
        listB.append(binary)
for element in listB:
    c = 0
    d = 0
    for i in range(n - 1, -1, -1):
        c += int(element[d]) * (2 ** i)
        d += 1
    answer.append(c)
print(max(answer))