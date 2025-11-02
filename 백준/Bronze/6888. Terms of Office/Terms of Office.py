start = int(input())
end = int(input())
list1 = [i for i in range(start, end + 1, 2)]
list2 = [i for i in range(start, end + 1, 3)]
list3 = [i for i in range(start, end + 1, 4)]
list4 = [i for i in range(start, end + 1, 5)]
for i in range(len(list4)):
    if(list4[i] in list1 and list4[i] in list2 and list4[i] in list3):
        print(f"All positions change in year {list4[i]}")