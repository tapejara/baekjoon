list1 = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
list2 = [input() for _ in range(3)]
print(int(str(list1.index(list2[0])) + str(list1.index(list2[1]))) * (10 ** list1.index(list2[2])))