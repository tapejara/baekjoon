n, k = map(int,input().split())
list1 = [int(input()) for _ in range(n)]
list1.sort()
answer = 0
while k > 0:
    a = list1.pop()
    if(a <= k):
        answer += k // a
        k %= a
print(answer)