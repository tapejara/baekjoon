a = int(input())
b = 1
c = 1
for i in range(a):
    if(b < a <= b + 6 * i):
        c += i
        break
    else:
        b += 6 * i
print(c)