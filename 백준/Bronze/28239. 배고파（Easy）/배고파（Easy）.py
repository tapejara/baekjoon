n = int(input())
for _ in range(n):
    m = int(input())
    for x in range(70):
        a= 2 ** x
        b = -1
        for y in range(70):
            c = 2 ** y
            if(a + c == m):
                print(x, y)
                b *= -1
                break
        if(b == 1):
            break