n = int(input())
a = 0
for _ in range(n):
    c = input()
    for i in range(1,len(c)):
        if(c[i - 1] == "0" and c[i] =="1") or (c[i - 1] == "O" and c[i] == "I"):
            a += 1
            break
print(a)