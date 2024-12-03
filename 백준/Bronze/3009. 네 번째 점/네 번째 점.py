a, b = map(int,input().split())
c, d = map(int,input().split())
e, f = map(int,input().split())
list1 = [a, c, e]
list2 = [b, d, f]
if(list1.count(a) == 1):
    print(a, end=" ")
elif(list1.count(c) == 1):
    print(c, end=" ")
elif(list1.count(e) == 1):
    print(e, end=" ")
if(list2.count(b) == 1):
    print(b)
elif(list2.count(d) == 1):
    print(d)
elif(list2.count(f) == 1):
    print(f)