n = int(input())
for _ in range(n):
    c = input()
    if(len(c) >= 6 and len(c) <= 9):
        print("yes")
    else:
        print("no")