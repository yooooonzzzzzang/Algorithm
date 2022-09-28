import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')
def binary_search()


for t in range(1, int(input()) + 1):
    n, m = map(int,input().split())     # a,b 개수
    a = list(map(int, input().split()))
    b = list(map(int,input().split()))
    cnt = 0
    binary_search(a, b)
    print(f'#{t} {cnt}')