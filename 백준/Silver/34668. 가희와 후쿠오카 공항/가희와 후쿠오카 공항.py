import sys
input = sys.stdin.readline
q = int(input())
for _ in range(q):
    m = int(input())
    time = m  // 50
    start = 366
    start += time * 12
    a = str(start // 60)
    b = str(start % 60)
    if(len(a) == 1):
        a = "0" + a
    if(len(b) == 1):
        b = "0" + b
    print(f"{a}:{b}")