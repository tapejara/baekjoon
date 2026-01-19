import math
dict = {"@":"a", "[":"c", "!":"i", ";":"j", "^":"n", "0":"o", "7":"t", "\\'":"v", "\\\\'":"w"}
n = int(input())
for _ in range(n):
    a = input()
    count_ex = 0
    point = ""
    answer = ""
    for c in a:
        if(96 < ord(c) < 123):
            answer += c
        elif(c in dict):
            answer += dict[c]
            count_ex += 1
        else:
            if(c == "\\"):
                point += "\\"
            else:
                point += c
            if(point in dict):
                answer += dict[point]
                point = ""
                count_ex += 1
    if(math.ceil(len(answer) / 2) <= count_ex):
        print("I don't understand")
    else:
        print(answer)