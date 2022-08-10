import sys

sys.stdin = open("input.txt")

t = 10

for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    candidate_max = []     # 합들을 넣을 리스트
    # 행의 합
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]
        candidate_max.append(sum_row)
    # 열의 합
    for j in range(100):
        sum_col = 0
        for i in range(100):
            sum_col += arr[i][j]
        candidate_max.append(sum_col)
    # 대각선의 합
    # 왼쪽 대각선
    left_cross = 0
    for i in range(100):
        left_cross += arr[i][i]
    candidate_max.append(left_cross)

    # 오른쪽 대각선
    right_cross = 0
    for i in range(100):
        right_cross += arr[i][100-1-i]
    candidate_max.append(right_cross)

    # 최대값 구하기
    sum_max = candidate_max[0]
    for i in range(1, len(candidate_max)):
        if sum_max < candidate_max[i]:
            sum_max = candidate_max[i]
    print(f'#{tc} {sum_max}')
