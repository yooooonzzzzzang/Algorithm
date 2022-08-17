import sys

sys.stdin = open('input.txt')


def pascal(n):
    mem = [[1], [1, 1]]

    for i in range(n):
        # i가 1 이하일 경우엔 그대로 출력
        # i가 1 초과일 경우에는 이전 리스트의 인접한 두 숫자의 합으로 구성된 새 리스트를 mem에 삽입
        if i > 1:
            mem.append([1, *[mem[i - 1][j - 1] + mem[i - 1][j] for j in range(1, len(mem[i - 1]))], 1])

        # 언패킹 연산자로 풀어서 출력
        print(*mem[i])


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    print(f'#{tc}')
    pascal(N)