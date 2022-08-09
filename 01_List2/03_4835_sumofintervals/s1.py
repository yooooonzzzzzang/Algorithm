import sys
sys.stdin = open("sample_input.txt")

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())    # 정수의 개수 N과 구간의 개수 M
    numbers = list(map(int, input().split()))   # n개의 정수를 담은 리스트
    max_nums = min_nums = 0
    for i in range(M):  # 임시로 M개 더한 max_nums 과 min_nums 생성
        max_nums += numbers[i]
        min_nums += numbers[i]

    for i in range(1, N-M+1):   # 더하기할 횟수
        temp = 0                # 임시로 더한 값을 저장할 temp
        for j in range(i, i+M):     # 구간의 개수만큼 numbers[j]가 증가하면서 합을 temp에 저장
            temp += int(numbers[j])
        if temp > max_nums:
            max_nums = temp
        if temp < min_nums:
            min_nums = temp

    print(f"#{tc} {max_nums - min_nums}")