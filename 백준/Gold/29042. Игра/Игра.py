a, b, c = map(int,input().split())
def function(x):
    list1 = []
    y = 2
    while y * 2 <= x:
        while x % y == 0:
            if(y <= c):
                list1.append(y)
            x //= y
        y += 1
    if(x != 1 and x <= c):
        list1.append(x) 
    return list1
list_a = function(a)
list_b = function(b)
if(len(list_a) > len(list_b)):
    print("First")
else:
    print("Second")