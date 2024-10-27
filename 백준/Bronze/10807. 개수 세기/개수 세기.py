a = int(input())
list = list(map(int,input().split()))
b = int(input())
i = 0
for element in list:
    if(element == b):
        i += 1
print(i)