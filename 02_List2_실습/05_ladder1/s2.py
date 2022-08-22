import sys

sys.stdin = open('input.txt', encoding='utf-8')
# 좌 우 상 (아래는 고려하지 않음)
dx, dy = [0, 0, -1], [-1, 1, 0]

for _ in range(10):
    t = input()
    ladder = [input().split() for _ in range(100)]

    # 1. 마지막 줄에서 x 지점 찾기
    for i, number in enumerate(ladder[-1]):
        if number == '2':
            x, y = 99, i    # 행, 열
            break
    # 2. 사다리 타고 올라가기
    while x > 0:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 확인 & 사다리 다음 위치가 1 인지
            if 0<= nx < 100 and 0 <= ny < 100 and ladder[nx][ny] == '1':
                ladder[x][y] = '0' # 전에 왔던 길 0 으로 바꿔줘서 돌아가지 못하게 해야함
                x, y = nx, ny

    print(f'#{t} {y}')