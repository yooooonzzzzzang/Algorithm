import sys

sys.stdin = open('1in.txt', encoding='utf-8')
dx, dy = [-1,1,0,0],[0,0,-1,1]  # 상하좌우

def func_abs(n):
    if n < 0:
        return -n
    else:
        return n

for t in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(n):

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<= nx < n and 0 <= ny < n :
                    total += func_abs(arr[nx][ny] - arr[i][j])


    print(f'#{t} {total}')