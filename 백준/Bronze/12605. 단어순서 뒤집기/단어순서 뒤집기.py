n = int(input())
for i in range(1, n + 1):
    list1 = list(input().split())
    list1.reverse()
    print(f"Case #{i}:", end = " ")
    for  c in list1:
        print(c, end = " ")
    print()