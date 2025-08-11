fibonacci = [1,2]
while fibonacci[-1] <= 10 ** 100:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
while True:
    a, b =map(int,input().split())
    if(a == 0 and b == 0):
        break
    count = 0
    for element in fibonacci:
        if(a <= element <= b):
            count += 1
    print(count)