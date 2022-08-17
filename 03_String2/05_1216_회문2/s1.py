import sys

sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1, 10 + 1):
    tc = int(input())
    arr = [input() for _ in range (100)]
    col_arr = []
    for i in range(100):
        line = []
        for j in range(100):
            line.append(arr[j][i])
        col_arr.append(line)

    for i in range(100):
        # 가로
        max = 0
        for j in range(100):
            for k in range(1,100):
                if arr[i][j: j+k] == arr[i][j: j+k][::1] and max < len(arr[i][j:j+k]):
                    max = len(arr[i][j:j+k])
                    i2, j2, k2 = i,j,k
            result = ''.join(arr[i2][j2:j2+k2])
        # 세로
    print(f'#{t} {result}')