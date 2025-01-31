n = int(input())
coin = 0
if(n % 2 == 1 and n >= 5):
    n -= 5
    coin += 1
elif(n % 2 == 1 and n < 5):
    print(-1)
    exit()
if(n // 10 >= 1):
    coin += n // 10 * 2
    n %= 10
coin += n // 2
print(coin)