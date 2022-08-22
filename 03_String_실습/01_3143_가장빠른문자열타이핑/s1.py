import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    result = 0  # 키를 누르는 최솟값
    A, B = input().split()

    result = len(A.replace(B, "*"))

    print(f'#{t} {result}')