import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    N = int(input())

    result = 0
    tree = [0] * (N + 1)

    # 루트에 저장된 값과, N/2번 노드에 저장된 값을 출력하는 프로그램
    print(f'#{t} {result}')
