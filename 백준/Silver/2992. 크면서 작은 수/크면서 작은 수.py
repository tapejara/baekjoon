from itertools import permutations
x = input()
list1 = [i for i in x]
list2 = []
for element in permutations(list1, len(list1)):
    temp = ""
    for num in element:
        temp += num
    if(len(list1) != len(str(int(temp))) or int(temp) in list2):
        continue
    list2.append(int(temp))
list2.sort()
answer = 0
for i in range(len(list2)):
    if(list2[i] > int(x)):
        answer = list2[i]
        break
print(answer)