import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    field = [input() for _ in range(n)]



    print(f'#{t} {}')