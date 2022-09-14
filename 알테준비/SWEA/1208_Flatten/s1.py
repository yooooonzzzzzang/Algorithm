import sys

sys.stdin = open('input.txt')

for t in range(1, 11):
    result = 0
    N = 100
    dump = int(input())
    arr = list(map(int, input().split()))
    for _ in range(dump):
        max_num = 0
        min_num = 0
        for i in range(len(arr)):
            if arr[max_num] < arr[i]:
                max_num = i
            elif arr[min_num] > arr[i]:
                min_num = i
        arr[max_num] -= 1
        arr[min_num] += 1

    real_max, real_min = 0, 10000000
    for i in range(100):
        if arr[i] > real_max:
            real_max = arr[i]
        elif arr[i] < real_min:
            real_min = arr[i]


    print(f'#{t} {real_max- real_min}')