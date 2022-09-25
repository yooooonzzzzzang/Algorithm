import sys

sys.stdin = open('input.txt')


# 절대값 구하는 함수
def get_abs(number):
    return number if number >= 0 else -number


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우

for t in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    total = 0  # 전체 칸의 합

    for x in range(n):
        for y in range(n):
            #temp = 0  # 한 칸의 합

            # 4방향 델타탐색
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]  # 다음 위치 이동
                if 0 <= nx < n and 0 <= ny < n:  # 범위 내 인가?
                    total += get_abs(board[nx][ny] - board[x][y])

            # total += temp

    print(f'#{t} {total}')