while True:
    a = int(input())
    b = 0
    list1 = []
    if(a == -1):
        break
    else:
        for i in range(1,a):
            if(a % i == 0):
                b += i
                list1.append(i)
        if(a == b):
            print(a, "=", end = " ")
            for i in range(len(list1)):
                if(i + 1 == len(list1)):
                    print(list1[i])
                else:
                    print(list1[i], "+",end = " ")
        else:
            print(a, "is NOT perfect.")    