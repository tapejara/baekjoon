a = int(input())
for i  in range(1,a + 1):
    b = ""
    b += " " * (a - i)
    b += "*" * i
    print(b)