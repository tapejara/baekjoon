n = int(input())
for i in range(1,n):
    a = str(i)
    s = 0
    for num in a:
        s += int(num)
    if(i + s == n):
        print(i)
        exit()
print(0)