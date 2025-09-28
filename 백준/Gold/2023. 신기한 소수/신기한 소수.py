n = int(input())
start = [1, 3, 5, 7, 9]
answer = []
def function(num):
    if(len(str(num)) == n):
        answer.append(num)
    else:
        for i in range(len(start)):
            temp = num * 10 + start[i]
            flag = True
            for j in range(2, int(temp**0.5) + 1):
                if(temp % j == 0):
                    flag = False
                    break
            if flag:
                function(temp)
for i in [2, 3, 5, 7]:
    function(i)
for element in answer:
    print(element)