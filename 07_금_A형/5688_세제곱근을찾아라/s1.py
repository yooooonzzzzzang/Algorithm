import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    result = -1
    N = int(input())

    for x1 in range(1, N+1):
        if x1 * x1* x1 == N:
            result = x1
            break
        if x1 * x1 * x1 > N:    # 제한시간초과 때문에 세제곱이 N보다 커지면 종료
            break

    print(f'#{t} {result}')