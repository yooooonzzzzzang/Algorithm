import sys
sys.stdin = open("input.txt")

t = int(input())    #테스트횟수

for tc in range(1, t+1):  #_ 변수 안쓸때 for _ in range(t)
    n = int(input()) #상자 줄 수
    numbers = list(map(int, input().split()))

    result = 0
    #나보다 높이 작을때 낙차+1
    for i in range(n): #0부터 n-1까지
        max_height = 0 #기준점

        for j in range(i+1, n): #기준점의 오른쪽에 작은게 있으면 낙차 + 1
            if numbers[i] > numbers[j]:
                max_height += 1

        if result < max_height:
            result = max_height

    print(f'#{tc} {result}')
