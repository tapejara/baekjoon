list1 = [0, 1, 1]
for _ in range(3, 491):
    list1.append(list1[-1] + list1[-2])
while True:
    n = int(input())
    if(n == -1):
        break
    print(f"Hour {n}: {list1[n]} cow(s) affected")