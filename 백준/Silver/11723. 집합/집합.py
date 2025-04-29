import sys
input = sys.stdin.readline
m = int(input())
set1 = set()
for _ in range(m):
    i = input().strip()
    if(" " in i):
        c, n = i.split()
        num = int(n)
        if(c == "add"):
            set1.add(num)
        elif(c == "remove" and num in set1):
            set1.remove(num)
        elif(c == "toggle"):
            if(num not in set1):
                set1.add(num)
            else:
                set1.remove(num)
        elif(c == "check"):
            if(num in set1):
                print(1)
            else:
                print(0)
    elif(i == "all"):
        set1 = set(i for i in range(1,21))
    elif(i == "empty"):
        set1.clear()