import sys 
input = sys.stdin.readline
while True:
    list1 = list(map(int,input().split()))
    if(list1[0] == 0):
        exit()
    n = list1.pop(0)
    list1.sort()
    list2 = list1.copy()
    while 0 in list2:
        list2.remove(0)
    a = str(list2.pop(0))
    b = str(list2.pop(0))
    list1.remove(int(a))
    list1.remove(int(b))
    while len(list1) > 0:
        a += str(list1.pop(0))
        if(len(list1) > 0):
            b += str(list1.pop(0))
    print(int(a) + int(b))