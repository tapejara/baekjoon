n = int(input())
for _ in range(n):
    list1 = [i for i in input()]
    a = 0
    for i in range(len(list1)):
        if(list1[i] == "U"):
            a += 1
        else:
            break
    print(a)