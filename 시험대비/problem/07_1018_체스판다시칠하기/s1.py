n, m = map(int, input().split()) # 행, 열
board =[]
for _ in range(n):
    board.append(input())

result = []
for i in range(n-7):      # n - k + 1
    for j in range(m-7):
        draw1 = 0   # 검은색을 칠한 횟수
        draw2 = 0   # 흰색을 칠한 횟수
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 2
                else:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 2
        result.append(min(draw1, draw2))
print(*result)

'''
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWWWB
BWBWBWBW

'''