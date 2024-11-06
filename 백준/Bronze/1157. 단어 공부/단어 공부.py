a = input()
b = a.lower()
list1 = list(b)
list2 = []
list3 = []
for i in range(97,123):
    list2.append(chr(i))
for c in list2:
    d = 0
    for element in list1:
        if(c == element):
            d += 1
    list3.append(d)
max_num = max(list3)
if(list3.count(max_num) >= 2):
    print("?")
else:
    f = list2[list3.index(max_num)]
    print(f.upper())