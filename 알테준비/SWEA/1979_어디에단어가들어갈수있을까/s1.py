import sys

sys.stdin = open('input (2).txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    words = list(input().split() for _ in range(n))
    # print(words)
    # 가로 찾기
    word =0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if words[i][j] == '1':
                    cnt += 1
            if words[i][j] == '0' or j == n-1:
                if cnt == k:
                    word += 1
                cnt = 0
    for j in range(n):
        for i in range(n):
            if words[i][j] == '1':
                    cnt += 1
            if words[i][j] == '0' or i == n-1:
                if cnt == k:
                    word += 1
                cnt = 0
    print(f'#{t} {word}')