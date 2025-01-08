a = int(input())
for i in range(a):
    b = input()
    list1 = []
    for element in b:
        list1.append(element)
        if(len(list1) >= 2 and list1[-1] == ")" and list1[-2] == "("):
            list1.pop()
            list1.pop()
    if(len(list1) == 0):
        print("YES")
    else:
        print("NO")