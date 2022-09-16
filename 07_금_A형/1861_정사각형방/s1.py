import sys
sys.stdin = open('input (1).txt')


def dfs(x, y):
    global cnt
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and room[nx][ny] == room[x][y] + 1:
            dfs(nx, ny)


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, int(input()) + 1):
    result = 0
    N = int(input())  # 정수 N
    room = [list(map(int, input().split())) for _ in range(N)]
    list_cnt = [0, 0]  # list_cnt[0]: 방번호, list_cnt[1]:방개수
    max_index = 0
    for i in range(N):
        for j in range(N):
            cnt = 0  # 방 개수
            dfs(i, j)
            if list_cnt[1] < cnt:  # 방 개수가 크면
                list_cnt[1] = cnt  # 리스트 1번에 다시 저장
                list_cnt[0] = room[i][j]  # 방 번호는 리스트 0번에 저장
            elif list_cnt[1] == cnt:  # 방 개수 같은 경우  -> 작은 방번호를 저장
                if list_cnt[0] > room[i][j]:
                    list_cnt[0] = room[i][j]

    print(f'#{t} {list_cnt[0]}', list_cnt[1])
