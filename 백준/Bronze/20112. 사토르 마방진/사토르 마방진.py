a = int(input())
list1 = []
list2 = []
for i in range(a):
    b = input()
    list1.append(b)
for i in range(a):
    c = ""
    for element in list1:
        c += element[i]
    list2.append(c)
for i in range(a):
    if(not list1[i] == list2[i]):
        print("NO")
        exit()
print("YES")