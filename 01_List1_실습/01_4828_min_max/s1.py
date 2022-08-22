import sys
sys.stdin = open("sample_input.txt")

t = int(input())    # 테스트 케이스 개수

for tc in range(1, t+1):
    n = int(input())    # 숫자 개수
    numbers = list(map(int, input().split()))

    maxnum = minnum = numbers[0]    # 리스트 0 번째를 maxnum, minnum 으로 임의지정
    for i in range(1, n):           # 1부터 (리스트 0번째는 이미 지정해줬으니까 안돌아도됨) n(숫자개수-1)까지(0번째는 안도니까 n+1 하지 않음)
        if numbers[i] > maxnum:     # numbers[i]: numbers[1]~ numbers[4] 이  maxnum (처음: numbers[0])과 비교하면서 더 크면
            maxnum = numbers[i]     # 더 큰 수를  maxnum 으로 변경

    for i in range(1, n):           # maxnum 과 같은 방법
        if numbers[i] < minnum:     # numbers[i]: numbers[1]~ numbers[4] 이  minnum (처음: numbers[0])과 비교하면서 더 작으면
            minnum = numbers[i]     # 더 작은 수를 minnum 으로 변경

    print(f'#{tc} {maxnum - minnum}')