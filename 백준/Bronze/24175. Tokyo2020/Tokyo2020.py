while True:
    a = int(input())
    if(a == 0):
        break
    list1 = []
    list2 = []
    for i in range(2022):
        list1.append(0)
        list2.append(0)
    for i in range(a):
        b, c, d = input().split()
        b1 = int(b)
        list1[b1] += 1
        if(d == "Gold"):
            list2[b1] += 1
    print(list2.index(max(list2)), list1.index(max(list1)))