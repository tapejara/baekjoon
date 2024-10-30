a,b = map(int,input().split())
list1 = [i for i in range(1,a+1)]
for i in range(b):
    c,d = map(int,input().split())
    list2 = list1[c-1:d]
    list2.reverse()
    list1[c-1:d] = list2
for element in list1:
    print(element,end=' ')