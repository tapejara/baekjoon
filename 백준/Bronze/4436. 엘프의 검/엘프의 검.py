import sys
input = sys.stdin.readline
while True:
    try:
        a = int(input())
        list1 = [ 0 for i in range(10)]
        b = 0
        while True:
            b += 1
            if("0" in str(a * b)):
                list1[0] = 1
            if("1" in str(a * b)):
                list1[1] = 1
            if("2" in str(a * b)):
                list1[2] = 1
            if("3" in str(a * b)):
                list1[3] = 1
            if("4" in str(a * b)):
                list1[4] = 1
            if("5" in str(a * b)):
                list1[5] = 1
            if("6" in str(a * b)):
                list1[6] = 1
            if("7" in str(a * b)):
                list1[7] = 1
            if("8" in str(a * b)):
                list1[8] = 1
            if("9" in str(a * b)):
                list1[9] = 1
            if(list1.count(1) == 10):
                print(b)
                break
    except:
        break