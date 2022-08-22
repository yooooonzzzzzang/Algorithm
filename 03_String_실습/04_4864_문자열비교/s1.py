import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    result = 0
    str1 = input()
    str2 = input()
    if str1 in str2:
        result = 1
    else:
        result = 0

    print(f'#{t} {result}')