n = int(input())
p = int(input())
list1 = [p for _ in range(4)]
if(n >= 5):
    list1[0]  -= 500
if(n >= 10):
   list1[1] -= list1[1] // 10
if(n >= 15):
    list1[2] -= 2000
if(n >= 20):
    list1[3] -= list1[3] * 25 // 100
answer = min(list1)
print(max(0, answer))