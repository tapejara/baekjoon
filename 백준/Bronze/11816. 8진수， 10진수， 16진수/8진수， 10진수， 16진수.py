n = input()
list1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
if(n[:2] == "0x"):
    answer = 0
    n = n[2:]
    n = [i for i in n]
    n.reverse()
    for i in range(len(n)):
        answer += list1.index(n[i]) * (16 ** i)
    print(answer)
elif(n[0] == "0"):
    answer = 0
    n = n[1:]
    n = [i for i in n]
    n.reverse()
    for i in range(len(n)):
        answer += int(n[i]) * (8 ** i)
    print(answer)
else:
    print(int(n))