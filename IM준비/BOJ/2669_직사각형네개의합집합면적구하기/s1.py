
board = [[0] * 100 for _ in range(100)]
for t in range(4):
    y1, x1, y2, x2 = map(int, input().split())

    for x in range(99-x1 ,99-x2):
        for y in range(99-y1, 99-y2):
            board[x][y] == 1
    for i in board:
        print(*i)