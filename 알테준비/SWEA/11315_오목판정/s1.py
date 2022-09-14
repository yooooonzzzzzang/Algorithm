import sys

sys.stdin = open('sample_input.txt')
#(→, ↓, ↘, ↙) 순으로 방향 dx, dy
dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]
def check():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 0
                    nx = i
                    ny = j
                    while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 'o':
                        cnt += 1
                        nx = nx + dx[k]
                        ny = ny + dy[k]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [input() for _ in range(n)]


    print(f'#{t} {check()}')