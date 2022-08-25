import sys

sys.stdin = open('sample_input.txt')
# N개의 숫자로 이뤄진 수열의 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for _ in range(M):  # M번 반복
        queue.append(queue.pop(0))

    print(f'#{t} {queue.pop(0)}')