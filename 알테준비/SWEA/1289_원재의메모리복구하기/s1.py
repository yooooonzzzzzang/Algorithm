import sys

sys.stdin = open('input (2).txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    result = 0
    target = input()
    n = len(target)
    data = ['0'] * n

    for i in range(n):
        if data[i] != target[i]:
            if data[i] == '0':
                value = '1'
            else:
                value ='0'
            for j in range(i, n):
                data[j] = value
            result += 1
        if ''.join(data) == target:
            break

    print(f'#{t} {result}')