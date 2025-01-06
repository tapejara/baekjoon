import sys
input = sys.stdin.readline
a = int(input())
list1 = []
for i in range(a):
    b = input()
    if("push" in b):
        c, d = b.split()
        list1.append(int(d))
    elif(b == "pop\n"):
        if(len(list1) == 0):
            print(-1)
        else:
            print(list1.pop(0))
    elif(b == "size\n"):
        print(len(list1))
    elif(b == "empty\n"):
        if(len(list1) == 0):
            print(1)
        else:
            print(0)
    elif(b == "front\n"):
        if(len(list1) == 0):
            print(-1)
        else:
            print(list1[0])
    elif(b == "back\n"):
        if(len(list1) == 0):
            print(-1)
        else:
            print(list1[-1])