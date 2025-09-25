n = int(input())
card = list(map(int,input().split()))
pa = 1
for i in card:
    pa *= i
base = [i for i in range(1,10)]
list1 = []
answer = []
def function(count, pb, arr1, arr2):
    if(count > n and pb > pa):
        answer.append(pb)
        list1.append(arr2)
        return 0
    elif(count > n):
        return 1
    else:
        for i in range(len(arr1)):
            arr3 = arr2.copy()
            arr3.append(arr1[i])
            if(function(count + 1, pb * arr1[i], arr1, arr3) == 0):
                return 0
function(1, 1, base, [])
if(list1):
    for element in list1[0]:
        print(element, end = " ")
else:
    print(-1)