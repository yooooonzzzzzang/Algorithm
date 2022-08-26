import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    result1 = 0
    result2 = 0

    # 1. 가로 검사
    for i in range(9):
        check = list(i+1 for i in range(9))     # 1~ 9 리스트
        for j in range(9):
            if arr[i][j] in check:
                check.remove(arr[i][j])
        if not check:
            result1 += 1
    if result1 == 9:
        result2 += 1
    result1 = 0 # 다음 검사에 쓰기위한 초기화

    # 2. 세로 검사
    for i in range(9):
        check = list(i+1 for i in range(9))
        for j in range(9):
            if arr[j][i] in check:
                check.remove(arr[j][i])
        if not check:
            result1 += 1
    if result1 == 9:
        result2 += 1
    result1 = 0 # 초기화

    # 3. 3 * 3 검사
    for i in range(0,9-3+1,3):
        for j in range(0,9-3+1,3):
            check = list(i+1 for i in range(9))
            for k in range(3):
                for l in range(3):
                    if arr[i+k][j+l] in check:
                        check.remove(arr[i+k][j+l])
            if not check:
                result1 += 1
    if result1 == 9:
        result2 += 1
    if result2 == 3:
        print(f'#{t} {1}')
    else:
        print(f'#{t} {0}')





