import sys
from itertools import combinations
sys.stdin = open('input (1).txt')

for t in range(1, int(input()) + 1):
    result = 0
    # N : 점원수  B : 선반 길이
    N, B = map(int,input().split())
    # clerk[] :  # 점원 키 저장
    clerk = list(map(int,input().split()))
    alist = list()  # 조건을 만족하는 결과값이 될 후보 리스트
    if N == 1:      # 직원이 한명일때
        result = 0
        break
    else:
        for i in range(2,N+1):  # 직원 수 2~ N명까지
            arr = list(combinations(clerk, i))  # 부분집합을 구하는 라이브러리함수
            for j in arr:
                total = 0
                for l in j:
                    total += l  # 부분집합의 합 구하기
                if total >= B:  # 선반의 길이보다 크거나 같으면
                    alist.append(total) # 결과값 후보에 넣는다
        result = min(alist)-B
    print(f'#{t} {result}')