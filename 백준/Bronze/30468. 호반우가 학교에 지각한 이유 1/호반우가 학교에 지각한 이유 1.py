s, d, i, l, n = map(int,input().split()) 
a = s + d + i + l
answer = 0
while a < 4 * n:
    answer += 1
    a += 1
print(answer)