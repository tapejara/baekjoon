list1 = []
list2 = []
for _ in range(9):
        a = list(map(int,input().split()))
        list1.append(a)
        list2.append(max(a))
b = 0
for i in range(9):
    if(max(list2) in list1[i]):
          b += i
          break      
c = list1[b].index(max(list2))
print(max(list2))
print(b + 1,c + 1)