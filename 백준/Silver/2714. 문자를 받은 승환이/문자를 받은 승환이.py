import sys
input = sys.stdin.readline
list1 = []
for i in range(27):
    temp = str(bin(i))[2:]
    code = "0" * (5 - len(temp)) + temp
    list1.append(code)
n = int(input())
for _ in range(n):
    r, c, m = input().split()
    r = int(r); c = int(c)
    spiral = [[] for _ in range(r)]
    for i in range(r):
        for j in range(i * c,(i + 1) * c):
            spiral[i].append(m[j])
    end_0 = c
    end_1 = r
    end_2 = -1
    end_3 = 0
    direction = 0
    letter = []
    point_x = 0
    point_y = 0
    count = 0
    while count < len(m):
        if(direction == 0):
            for i in range(point_x, end_0):
                letter.append(spiral[point_y][i])
                point_x += 1
                count += 1
            point_x -= 1
            point_y += 1
            end_0 -= 1
            direction = 1
        elif(direction == 1):
            for i in range(point_y, end_1):
                letter.append(spiral[i][point_x])
                point_y += 1
                count += 1
            point_x -= 1
            point_y -= 1
            end_1 -= 1
            direction = 2
        elif(direction == 2):
            for i in range(point_x, end_2, -1):
                letter.append(spiral[point_y][i])
                point_x -= 1
                count += 1
            point_x += 1
            point_y -= 1
            end_2 += 1
            direction =3
        if(direction == 3):
            for i in range(point_y, end_3, -1):
                letter.append(spiral[i][point_x])
                point_y -= 1
                count += 1
            point_x += 1
            point_y += 1
            end_3 += 1
            direction = 0
    letter.reverse()
    answer = ""
    for i in range(len(m) // 5):
        alph = ""
        for j in range(5):
            alph += letter.pop()
        if(list1.index(alph) != 0):
            answer += chr(list1.index(alph) + 64)
        else:
            answer += " "
    print(answer.strip())