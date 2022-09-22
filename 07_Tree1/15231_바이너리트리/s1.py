import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    N, V = map(int, input().split())
    print(N, V)
    print(f'#{t} ')