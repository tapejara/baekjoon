n = int(input())
answer = 1
while True:
    if(answer ** 2 > n):
        print(f"The largest square has side length {answer - 1}.")
        exit()
    else:
        answer += 1