a = input()
b = a[::-1]
c = 0
for i in range(len(a)):
    if(a[i] != b[i]):
        print(0)
        c -= c
        break
    else:
        c += 1
if(c >= 1):
    print(1)