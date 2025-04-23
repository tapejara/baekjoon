while True:
    list1 = list(map(int,input().split()))
    if(list1.count(0) == 3):
        break
    list1.sort()
    if(list1[0] ** 2 + list1[1] ** 2 == list1[2] ** 2):
        print("right")
    else:
        print("wrong")