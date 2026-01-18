set_b = set("1")
set_w = set()
for i in range(2,65):
    if(((i - 1) // 8) % 2 == 0):
        if(i % 2 == 0):
            set_w.add(str(i))
        else:
            set_b.add(str(i))
    else:
        if(i % 2 == 0):
            set_b.add(str(i))
        else:
            set_w.add(str(i))
temp = ["A", "B", "C", "D", "E", "F", "G", "H"]
count = 1
for i in range(1,9):
    for c in temp:
        if(str(count) in set_b):
            set_b.add(c + str(i))
            count += 1
        else:
            set_w.add(c + str(i))
            count += 1
t = int(input())
for _ in range(t):
    a, b = input().split()
    if((a in set_b and b in set_b) or (a in set_w and b in set_w)):
        print("YES")
    else:
        print("NO")