import sys

sys.stdin = open('input (1).txt', encoding='utf-8')
dx =[-1,1,0,0]
dy =[0,0,-1,1]
for t in range(1, int(input()) + 1):
    n = int(input())
    cont = 0
    total = []
    rooms = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<= nx < n and 0 <= ny < n and rooms[nx][ny]-1 == rooms[i][j]:
                    i, j = nx, ny
                    cont += 1
                else:
                    total.append(cont)
                    cont = 0
    print(f'#{t} ',max(total))