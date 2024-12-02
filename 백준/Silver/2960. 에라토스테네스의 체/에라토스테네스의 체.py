a,b = map(int,input().split()) 
c = 0
list1 = []
for i in range(2, a + 1):
    for j in range(1, a // i + 1):
        d = i * j
        if not d in list1:
            list1.append(d)
            c += 1
            if b == c:
                print(d)
                break