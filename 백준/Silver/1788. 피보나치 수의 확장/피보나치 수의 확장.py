n = int(input())
a = 1000000000
fibonacci = [0,1]
if(n > 0):
    for _ in range(1, n):
        fibonacci.append((fibonacci[0] % a + fibonacci[1] % a) % a)
        fibonacci.pop(0)
    print(1)
    print(fibonacci[1])
elif(n == 0):
    print(0)
    print(0)
else:
    for _ in range(1,abs(n)):
        fibonacci.append((fibonacci[0] % a + fibonacci[1] % a) % a)
        fibonacci.pop(0)
    if(abs(n) % 2 == 0):
        print(-1)
    else:
        print(1)
    print(fibonacci[1])