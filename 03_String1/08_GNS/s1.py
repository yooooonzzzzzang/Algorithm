import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR','FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    TC, LEN = input().split()
    arr = list(input().split())
    print(f'#{t}')
    count_n = [0 for i in range(10)]
    for i, j in enumerate(nums):     # 숫자 개수 세주기
        count_n[i] = arr.count(j)

    for i, j in enumerate(count_n):
        print((nums[i] + ' ') * j, end='')
    print()