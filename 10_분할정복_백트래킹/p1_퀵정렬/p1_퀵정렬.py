import sys

sys.stdin = open('input.txt')

def partition(l,r):
    pivot = arr[l]
    i = l
    j = r
    while i <= j:
        while i<=j and arr[i] <= pivot:
            i += 1
        while i<=j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def qsort(l,r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)

for t in range(1, int(input()) + 1):
    result = 0
    arr = list(map(int,input().split()))
    n = len(arr)
    qsort(0, n-1)
    print(f'#{t} {arr}')