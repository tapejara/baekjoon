list1 = []
for i in range(3):
    a = int(input())
    list1.append(a)
if(sum(list1) > 180 or sum(list1) < 180):
    print("Error")
elif(list1[0] == list1[1] == list1[2]):
    print("Equilateral")
elif(list1[0] == list1[1] or list1[0] == list1[2] or list1[1] == list1[2]):
    print("Isosceles")
else:
    print("Scalene")