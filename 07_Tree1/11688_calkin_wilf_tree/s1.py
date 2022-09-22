import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')


for t in range(1, int(input()) + 1):
    arr = input()
    a, b = 1, 1
    for i in arr:
        if i == 'L':
            b = a + b
        else:   # R 일때
            a = a + b
    print(f'#{t} {a} {b}')