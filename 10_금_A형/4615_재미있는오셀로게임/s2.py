import sys
sys.stdin = open("sample_input(1).txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    # 8가지 방향을 담음
    delta = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    # 초기 설정
    mid = N // 2
    arr[mid][mid] = 2
    arr[mid - 1][mid - 1] = 2
    arr[mid][mid - 1] = 1
    arr[mid - 1][mid] = 1
    for _ in range(M):
        # 행렬 좌표 값이 설명에서 나온 좌표값과 반대
        # 헷갈림 방지를 위해 뒤집어서 받음
        y, x, color = map(int, input().split())
        y -= 1
        x -= 1
        # 돌을 놓을 곳이 없다면 다음 턴으로 넘어간다

        if not arr[x][y]:
            arr[x][y] = color
            for i in range(8):
                dx, dy = delta[i]
                nx, ny = x + dx, y + dy
                # 뒤집을 좌표를 저장
                reverse = []
                while True:
                    # 다음 검사 값이 배열 안에 있는지 확인
                    if nx < 0 or N - 1 < nx or ny < 0 or N - 1 < ny:
                        reverse = []
                        break
                    # 공백이 아닌지 확인
                    if arr[nx][ny] == 0:
                        reverse = []
                        break
                    # 같은 색깔을 만났다면 멈춤
                    if arr[nx][ny] == color:
                        break
                    # 다른 색이라면 좌표를 저장한다.
                    else:
                        reverse.append((nx, ny))
                    nx += dx
                    ny += dy
                    print(nx, ny)
                # 색을 뒤집어준다.
                for rx, ry in reverse:
                    arr[rx][ry] = color
    # 돌을 다 놓았다면 배열들 돌며 흰돌, 검은돌의 갯수를 세어준다.
    W, B = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                W += 1
            elif arr[i][j] == 2:
                B += 1

    print('#{} {} {}'.format(tc, W, B))