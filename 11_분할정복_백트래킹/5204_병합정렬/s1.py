import sys

sys.stdin = open('sample_input.txt')
def merge(l_arr, r_arr):
    merged_arr = []
    i, j = 0, 0

    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] <= r_arr[j]:
            merged_arr.append(l_arr[i])
            i += 1
        else:
            merged_arr.append(r_arr[j])
            j += 1
    merged_arr.extend(l_arr[i:])
    merged_arr.extend(r_arr[j:])
    return merged_arr

def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    l_arr = merge_sort(arr[:mid])
    r_arr = merge_sort(arr[mid:])
    if l_arr[-1] > r_arr[-1]:
        cnt += 1
    return merge(l_arr,r_arr)


for t in range(1, int(input()) + 1):
    n = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    answer = merge_sort(A)
    print(f'#{t} {answer[n//2]} {cnt}')