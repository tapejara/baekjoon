a = input()
list1 = a.split(' ')
if(list1[0] == ''):
    del list1[0]
if(list1[-1] == ''):
    del list1[-1]
print(len(list1))