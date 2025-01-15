from itertools import permutations
yumi = list(map(int,input().split()))
person1 = list(map(int,input().split()))
person2 = list(map(int,input().split()))
person3 = list(map(int,input().split()))
total = [person1, person2, person3]
answer = []
permut = list(permutations(total,3))
for i in range(len(permut)):
    space = 0
    space += ((yumi[0] - permut[i][0][0]) ** 2 + (yumi[1] - permut[i][0][1]) ** 2) ** 0.5
    space += ((permut[i][0][0] - permut[i][1][0]) ** 2 + (permut[i][0][1] - permut[i][1][1]) ** 2) ** 0.5
    space += ((permut[i][1][0] - permut[i][2][0]) ** 2 + (permut[i][1][1] - permut[i][2][1]) ** 2) ** 0.5
    answer.append(int(space))
print(min(answer))