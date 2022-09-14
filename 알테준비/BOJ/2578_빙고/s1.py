arr = [list(map(int, input().split())) for _ in range(5)]
answer = 0
call = [list(map(int, input().split())) for _ in range(5)]
def check_row(li):
    answer = 0
    for row in range(5):
        if sum(li[row]) == 0:
            answer += 1
    return answer
def check_col(li):
    answer = 0
    for col in range(5):
        sum_value = 0
        for row in range(5):
            sum_value += li[row][col]
        if sum_value == 0:
            answer += 1
    return answer
def check_x(li):
    answer = 0
    slash = 0
    back_slash = 0
    for i in range(5):
        slash += li[i][i]
        back_slash += li[i][4 - i]
    if slash == 0:
        answer += 1
    if back_slash == 0:
        answer += 1
    return answer


cnt = 0
for row in range(5):
    for col in range(5):
        cnt += 1
        call_num = call[row][col]

        for i in range(5):
            for j in range(5):
                if arr[i][j] == call_num:
                    arr[i][j] = 0
                    break
        row_cnt = check_row(arr)
        col_cnt = check_col(arr)
        x_cnt = check_x(arr)

        if row_cnt + col_cnt + x_cnt >= 3:
            answer = cnt
            break
    if answer!= 0:
        break
print(answer)
