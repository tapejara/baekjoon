a = int(input())
if(a == 1):
    exit()
else:
    list1 = []
    while a % 2 == 0 and a >= 2:
        a = a // 2
        list1.append(2)
    i = 3
    while a >= i:
        if(a % i == 0):
            a = a // i
            list1.append(i)
        else:
            i += 2    
    for element in list1:
        print(element)