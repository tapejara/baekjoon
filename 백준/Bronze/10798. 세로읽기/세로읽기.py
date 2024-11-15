list1 = []
list2 = []
list3 = []
for i in range(5):
    list1.append(input())
    list2.append(len(list1[i]))
for i in range(5):
    if(list2[i] < max(list2)):
        list1[i] += "@" * (max(list2) - list2[i])
        list3.append(list1[i])
    else:
        list3.append(list1[i])
for i in range(max(list2)):
    for j in range(5):
        if(not list1[j][i] == "@"):
            print(list1[j][i], end = "")