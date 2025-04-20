import sys
input = sys.stdin.readline
prime_list = [i for i in range(2, 10001)]
for i in range(2,100):
    if(i in prime_list):
        for j in range(i * 2, 10001, i):
            if(j in prime_list):
                prime_list.remove(j)
prime_set = set(prime_list)
t = int(input())
for _ in range(t):
    n = int(input())
    list1 = []
    temp = 0
    for element in prime_list:
        if(element > n // 2):
            temp = prime_list.index(element)
            break
    for i in range(temp):
        if(n - prime_list[i] in prime_set):
            list1.append((prime_list[i], n - prime_list[i]))
    answer = list1.pop()
    print(answer[0], answer[1])