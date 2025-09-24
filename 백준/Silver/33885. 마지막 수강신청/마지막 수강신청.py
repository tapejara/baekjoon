n, m = map(int,input().split())
temp = [list(input().split()) for _ in range(n)]
day = ["MON", "TUE", "WED", "THU", "FRI"]
time = [[] for _ in range(n)]
score = []
list1 = [i for i in range(n)]
list2 = [[] for _ in range(5)]
answer = [0]
for i in range(n):
    score.append(int(temp[i][0]))
    for j in range(2, 2 + int(temp[i][1]) * 2, 2):
        time[i].append((day.index(temp[i][j]), int(temp[i][j + 1])))
def function(count, arr1, arr2):
    if(len(arr2) == 1):
        flag = True
        for i in range(len(time[arr2[0]])):
            if(time[arr2[0]][i][1] in arr1[time[arr2[0]][i][0]]):
                flag = False
        if(flag == True):
            answer.append(count + score[arr2[0]])
    else:
        for i in range(len(arr2)):
            flag = True
            for j in range(len(time[arr2[i]])):
                if(time[arr2[i]][j][1] in arr1[time[arr2[i]][j][0]]):
                    flag = False
            if(flag == True):
                arr3 = []
                for k in range(len(arr1)):
                    temp2 = arr1[k].copy()
                    arr3.append(temp2)
                for j in range(len(time[arr2[i]])):
                    arr3[time[arr2[i]][j][0]].append(time[arr2[i]][j][1])
                answer.append(count + score[arr2[i]])
                function(count + score[arr2[i]], arr3, arr2[i + 1:])
function(0, list2, list1)
if(max(answer) >= m):
    print("YES")
else:
    print("NO")