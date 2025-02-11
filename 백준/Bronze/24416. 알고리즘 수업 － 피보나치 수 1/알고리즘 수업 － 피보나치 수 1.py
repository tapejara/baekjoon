n = int(input())
count = [1, 0]
def function(x):
    if(x == 1 or x == 2):
        return 1
    else:
        count[0] += 1
        return function(x - 1) + function(x - 2)
list1 = [1,1]
for i in range(2,n):
    count[1] += 1
    list1.append(list1[i - 1] + list1[i - 2])
function(n)
print(count[0], count[1])