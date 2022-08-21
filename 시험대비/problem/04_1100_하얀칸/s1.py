# 하얀칸 위에 있는 말
total = 0
board = [input() for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:     # 짝수줄
            if board[i][j] == 'F':
                total += 1
        elif i % 2 == 1 and j % 2 == 1:               # 홀수줄
            if board[i][j] == 'F':
                total += 1
print(total)

# 행이 홀수줄 흰검흰검
# 행이 짝수줄 검흰검흰