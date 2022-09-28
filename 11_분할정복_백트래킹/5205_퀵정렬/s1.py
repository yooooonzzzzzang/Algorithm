import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

def partition(l,r):
    pivot = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def qsort(l,r):
    if l<r:
        s = partition(l,r)
        qsort(l, s-1)
        qsort(s+1,r)


for t in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int,input().split()))
    qsort(0, n-1)
    print(f'#{t} {arr[n//2]}')