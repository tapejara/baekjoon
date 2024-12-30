a = int(input())
for _ in range(a):
    b = 0
    c = ""
    s,p = input().split()
    for i in range(len(s)):
        c += s[i]
        if(p in c):
            b += 1
            c = ""
    d = s.replace(p,"")
    b += len(d)
    print(b)