answer = 0
a,b = input().split()
for i in range(len(a)):
    if(64 < ord(a[i]) < 91):
        answer += (ord(a[i]) - 55) * (int(b) ** (len(a) - i - 1))
    elif(47 < ord(a[i]) < 58):
        answer += int(a[i]) * (int(b) ** (len(a) - i - 1))
print(answer)