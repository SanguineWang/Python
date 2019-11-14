import random
##开始菜单
def start():
    print("主菜单\n")
    print("1:单人游戏 2：双人游戏\n")
    while True:
        inp = input("请选择:")
        if inp=="1"or inp=="2":
            break
    return inp
##初始化棋盘
def initboard():
    list = [[0 for i in range(3)] for j in range(3)]##创建二维数组
    count = 1
    for i in range(3):
        for j in range(3):
            list[i][j] = count
            count = count + 1
        ##print(list[i])
    return list
#打印棋盘，可调格式
def printboard(list):
    for i in range(3):
        print("———————")
        print("|", list[i][0], "|", list[i][1], "|", list[i][2], "|")
    print("———————")
    return 0
#游戏开始并传入选择模式代表的数字
def game(inp):
    over=0
    if inp == "1":
        person0=input("玩家：\n")
        cp="computer"
        ran = random.randint(1, 2)
        print("随机判定：")
        print(ran)
        if ran == 1:
            print(person0 + "先手" + "执⚪")
            print(cp + "后手" + "执×")
            winner = pk1(person0, cp)
            print("winner:")
            print(winner)
        elif ran == 2:
            print(cp + "先手" + "执⚪")
            print(person0 + "后手" + "执×")
            winner = pk1(cp, person0)
            print("winner:")
            print(winner)
    elif inp =="2":
        person1=input("玩家1：\n")
        person2=input("玩家2：\n")
        ran = random.randint(1, 2)
        print(ran)
        print("随机判定：")
        if ran == 1:
            print(person1 + "先手" + "执⚪")
            print(person2 + "后手" + "执×")
            winner = pk2(person1, person2)
            print("winner:")
            print(winner)
        elif ran == 2:
            print(person2 + "先手" + "执⚪")
            print(person1 + "后手" + "执×")
            winner = pk2(person2, person1)
            print("winner:")
            print(winner)
    return 0
#对局
def pk1(persion1,persion2):
    board = initboard()
    printboard(board)
    winner = "none"

    round=0
    while True:
        round=round+1
        if persion1 == "computer" or round > 1:
            cp = random.randint(1, 9)
            i = (cp - 1) / 3
            j = (cp - 1) % 3
            i = int(i)
            print(i, j)
            while board[i][j] == "⚪" or board[i][j] == "×":
                cp = random.randint(1, 9)
                i = (cp - 1) / 3
                j = (cp - 1) % 3
                i = int(i)
                print(i, j)
            board[i][j] = "⚪"
            printboard(board)
            if check(board, i, j) > 0:
                winner = persion1
                break

        p=input(persion2+"请输入落子区域编号：\n")
        i = (int(p)-1) / 3
        j = (int(p)-1) % 3
        i = int(i)
        print(i,j)
        while board[i][j] == "⚪" or board[i][j] == "×":
            p = input(persion2 + "请重新输入落子区域编号：\n")
            i = (int(p) - 1) / 3
            j = (int(p) - 1) % 3
            i = int(i)
            print(i, j)
        board[i][j] = "×"
        printboard(board)
        if check(board,i,j)>0:
            winner = persion2
            break
    return winner
def pk2(persion1,persion2):
    board = initboard()
    printboard(board)
    winner="none"
    while True:
        p1=input(persion1+"请输入落子区域编号：\n")
        i=(int(p1)-1)/3
        j=(int(p1)-1)%3
        i=int(i)
        print(i, j)
        while board[i][j]=="⚪" or board[i][j]=="×":
            p1 = input(persion1 + "请重新输入落子区域编号：\n")
            i = (int(p1) - 1) / 3
            j = (int(p1) - 1) % 3
            i = int(i)
            print(i, j)
        board[i][j]="⚪"
        printboard(board)
        if check(board,i,j)>0:
            winner=persion1
            break
        p2=input(persion2+"请输入落子区域编号：\n")
        i = (int(p2)-1) / 3
        j = (int(p2)-1) % 3
        i = int(i)
        print(i,j)
        while board[i][j] == "⚪" or board[i][j] == "×":
            p2 = input(persion2 + "请重新输入落子区域编号：\n")
            i = (int(p2) - 1) / 3
            j = (int(p2) - 1) % 3
            i = int(i)
            print(i, j)
        board[i][j] = "×"
        printboard(board)
        if check(board,i,j)>0:
            winner = persion2
            break
    return winner
#判定，传入块号代表的行和列
def check(board,i,j):
    #对角线横竖对角检查
    if i==j or i == (j%2):
        #横竖检查
        heng = 0
        for colum in range(3):
            if board[i][j] == board[i][colum]:
                heng = heng + 1
        shu = 0
        for row in range(3):
            if board[i][j] == board[row][j]:
                shu = shu + 1
        if shu == 3 or heng == 3:
            return 1
        #对角检查
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return 1
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return 1
    return -1
if __name__ == '__main__':
    star=start()
    game(star)