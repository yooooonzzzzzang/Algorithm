import sys


def chk(num):
    num_St = str(num)
    for j in range(1, len(num_St)):
        if num_St[j] < num_St[j-1]:
            return False
    return True


sys.stdin = open('s_input.txt')


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    mul = []

    for i in range(N-1):
        for j in range(i+1, N):
           mul.append(arr[i] * arr[j])

    temp = 0
    for i in mul:
        if chk(i):
            if temp < i:
                temp = i

    print(f'#{t} {temp}')