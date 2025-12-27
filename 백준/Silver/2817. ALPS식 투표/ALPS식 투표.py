x = int(input())
n = int(input())
list0 = []
list1 = [0] * 26
for i in range(n):
    a, b = input().split()
    if(int(b) >= x * 5 // 100):
        list1[ord(a) - 65] += 1
        for j in range(1, 15):
            list0.append((int(b) // j, ord(a) - 65))
list0.sort(reverse=True)
for i in range(14):
    list1[list0[i][1]] += 1
for i in range(len(list1)):
    if(list1[i] > 0):
        print(chr(i + 65), list1[i] - 1)