board = [list(map(int, input().split())) for _ in range(9)]
max_num = max_x = max_y = 0
for x in range(9):
    for y in range(9):
        if max_num < board[x][y]:
            max_num = board[x][y]
            max_x, max_y = x, y

print(max_num)
print(max_x+1, max_y+1)