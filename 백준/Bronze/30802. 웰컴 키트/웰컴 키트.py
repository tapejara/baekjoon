n = int(input())
list1 = list(map(int,input().split()))
t, p = map(int,input().split())
answer_t = 0
for element in list1:
    if(element % t != 0):
        answer_t += element // t + 1
    else:
        answer_t += element // t
answer_p = n // p
other = n % p
print(answer_t)
print(answer_p, other)