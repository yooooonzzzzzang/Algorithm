import sys

sys.stdin = open('input (2).txt', encoding='utf-8')

for t in range(1, 10 + 1):
    tc = int(input())
    nums = list(map(int, input().split()))

    flag = False
    while True:
        for i in range(1, 6):   # 1~5번
            num = nums.pop(0)-i
            if num <= 0:
                nums.append(0)
                flag = True
                break
            else:
                nums.append(num)
        if flag:
            break
    print(f'#{t}', *nums)