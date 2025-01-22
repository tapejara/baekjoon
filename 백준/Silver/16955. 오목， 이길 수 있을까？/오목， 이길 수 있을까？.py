board = []
for _ in range(10):
    a = input()
    list1 = [element for element in a]
    board.append(list1)
def function():
    for k in range(10):
        for l in range(10):
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            if(board[k][l] == "X"):
                if(l < 6):
                    for m in range(5):
                        if(board[k][l + m] == "X"):
                            count1 += 1
                if(count1 == 5):
                    print(1)
                    exit()
                if(k < 6):
                    for m in range(5):
                        if(board[k + m][l] == "X"):
                            count2 += 1
                if(count2 == 5):
                    print(1)
                    exit()
                if(l > 3 and k < 6):
                    for m in range(5):
                        if(board[k + m][l - m] == "X"):
                            count3 += 1
                if(count3 == 5):
                    print(1)
                    exit()
                if(l < 6 and k < 6):
                    for m  in range(5):
                        if(board[k + m][l + m] == "X"):
                            count4 += 1
                if(count4 == 5):
                    print(1)
                    exit()
for i in range(10):
    for j in range(10):
        if(board[i][j] == "."):
            board[i][j] = "X"
            function()
            board[i][j] = "."
print(0)