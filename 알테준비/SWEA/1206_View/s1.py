import sys

sys.stdin = open('input.txt')

for t in range(1, 10 + 1):
    result = 0
    N = int(input())    # 건물의 개수
    buildings = list(map(int, input().split()))

    for i in range(2, N-2):
        max_num = 0
        for j in range(i-2, i+3):
            if i == j:
                continue
            if max_num < buildings[j]:
                max_num = buildings[j]

        if max_num < buildings[i]:
            result += buildings[i] - max_num
    print(f'#{t} {result}')