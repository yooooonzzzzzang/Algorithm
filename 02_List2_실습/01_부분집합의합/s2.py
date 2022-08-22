import sys

sys.stdin = open('sample_input (1).txt')

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    result = 0
    # 1. 부분 집합 개수만큼 반복 (모든 부분집합 본다)     2**4 == 1<<4
    for i in range(1, 1<<12):
        length, total = 0, 0

    # 2. 몇 번째 원소를 선택할지 결정
        for j in range(12):  # 하나의 부분집합
            if i & (1 << j):
                length += 1
                total += j + 1
    # 3. 조건을 만족하면(N개, 합이 K) ->  결과값 + 1
        if length == n and total == k:
            result += 1
    print(f'#{t} {result}')