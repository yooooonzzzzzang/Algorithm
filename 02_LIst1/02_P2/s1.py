import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    arr = list(map(int, input().split()))
    n = 10
    result = 0  # 결과값 초기화 (0 or 1 로 나와야함)
    for i in range(1, 1<<n):    # 비트 연산자를 이용해서 부분집합 생성 /1부터 시작 =>공집합 제외
        total = 0
        for j in range(n):
            if i & (1<<j):
                total += arr[j] # total 에 부분집합원소들을 저장
        if total == 0:  # 합이 0 이면 결과값 1
            result = 1
    print(f'#{tc} {result}')