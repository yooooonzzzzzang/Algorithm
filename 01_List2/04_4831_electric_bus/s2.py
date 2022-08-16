import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split()))
    start, end = 0, k
    # 충전기가 있는지
    is_possible = True
    result = 0

    while end < n : # 도착하지 않은 경우동안 반복
        if not is_possible:
            result = 0
            break
        for i in range(end, start, -1):
            # 1. 충전소가 있으면
            if i in stations:
                start = i
                end = start + k
                result += 1
                break #for 탈출
        else:
            # 2. 충전소가 없으면
            is_possible = False
    print(f'#{t} {result}')