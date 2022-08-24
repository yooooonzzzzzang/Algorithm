import sys

sys.stdin = open('input.txt')

for t in range(1, 11):
    result = 0
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range (100)]
    result =[]
    cross1_sum, cross2_sum = 0, 0
    # 행의 합
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            # ↘ 의 합
            if i == j:
                cross1_sum += arr[i][j]
        result.append(row_sum)
        result.append(cross1_sum)

    # 열의 합
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]
        result.append(col_sum)

    # ↙ 의 합
    for i in range(100): # 0 ~ 99
        cross2_sum += arr[i][99-i]
    result.append(cross2_sum)

    print(f'#{t} {max(result)}')
