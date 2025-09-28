n = int(input())
start = ["1","2","3","4","5","6","7","8","9"]
answer = []
def function(count, arr1, num):
    if(count > n):
        answer.append(int(num))
    else:
        for i in range(len(arr1)):
            temp = num + arr1[i]
            flag = True
            for j in range(2,int(temp) // 2):
                if(int(temp) % j == 0):
                    flag = False
                    break
            if flag:
                function(count + 1, arr1, temp)
for i in ["2","3","5","7"]:
    function(2, start, i)
for element in answer:
    print(element)