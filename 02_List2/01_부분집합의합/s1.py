import sys

sys.stdin = open("sample_input (1).txt")

t = int(input())

for tc in range(1, t + 1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, k = map(int, input().split())    # N:부분집합의 원소 개수 K: 원소의 합

    cnt = 0
    # 부분집합 생성
    for i in range(1, 1 << len(A)):     # 공집합을 제외한 모든 부분집합 검사 2**12
        arr = []    # 부분집합을 담을 리스트
        total = 0
        for j in range(len(A)): # A의 모든 원소 루프
            if i & (1 << j):    # i 의 j번째 비트 검사, j번째 비트가 1이면 A[j] 출력
               arr += [A[j]]
               total += A[j]
        if len(arr) == N and total == k:    # 부분집합 원소의 개수가 N이고 합이 k이면 cnt 값 1 증가
            cnt += 1
    print('#{} {}'.format(tc, cnt))