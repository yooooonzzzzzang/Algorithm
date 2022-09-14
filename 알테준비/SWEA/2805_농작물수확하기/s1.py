import sys

sys.stdin = open('input (2).txt')

for t in range(1, int(input()) + 1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    result = 0

    # s: 시작포인트, e: 끝포인트
    s, e = N // 2, N // 2
    for i in range(N):
        for j in range(s, e + 1):
            result += a[i][j]
        # 행의 인덱스가 mid 전까지는 s-e 간격 늘리고 mid 이후로는 간격 줄임
        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(f'#{t} {result}')