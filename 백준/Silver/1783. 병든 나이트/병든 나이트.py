n, m = map(int,input().split())
if(n == 1):
    print(1)
elif(n == 2):
    print(min(4,(m + 1) // 2))
elif(n >= 3):
    if(m < 5):
        print(m)
    elif(m <= 6):
        print(4)
    else:
        print((m - 7) + 5)