while True:
    list1 = list(map(int,input().split()))
    if(list1[0] == 0 and list1[1] == 0 and list1[2] == 0):
        break
    else:
        if((sum(list1) - max(list1)) <= max(list1) ):
            print("Invalid")
        elif(list1[0] == list1[1] == list1[2]):
            print("Equilateral ")
        elif(list1[0] == list1[1] or list1[0] == list1[2] or list1[1] == list1[2]):
            print("Isosceles")
        else:
            print("Scalene")