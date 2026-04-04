list1 = [0]* 2
for _ in range(9):
    c = input()
    if(c == "Lion"):
        list1[0] += 1
    else:
        list1[1] += 1
if(list1[0] > list1[1]):
    print("Lion")
else:
    print("Tiger")