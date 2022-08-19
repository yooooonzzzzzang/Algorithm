import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    N = int(input())    # 카드 개수
    result = []

    cards = input().split()     # n 개의 카드
    if N % 2 == 0:  # 짝수
        first = second = N // 2
    else:   # 홀수
        first, second = N // 2 + 1, N//2
    first_card = cards[0:first]
    second_card = cards[first:]

    for i in range(N):
        if i % 2 == 0:
            result.append(first_card[0])
            del first_card[0]
        else:
            result.append(second_card[0])
            del second_card[0]
    print(f'#{t}',*result)