def partition(l,r):
    pivot = A[l]    # 피봇이 첫번째에 있을때
    i,j=l,r
    while i <= j:
        # 1. 피벗보다 큰 값이 나올 때까지 i + 1
        while i<=j and A[i] <= pivot:
            i += 1
        # 2. 피벗보다 작은 값이 나올 때까지 j - 1
        while i<=j and A[j] >= pivot:
            j -= 1
        # 3. 피벗보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 교환
        if i < j:
            A[i], A[j] = A[j], A[i]
    # i > j가 되면 피벗과 j 위치 원소 교환 (피벗을 가운데로 옮기는 작업)
    A[l], A[j] = A[j], A[l]
    return j


def qsort(l,r):
    if l < r:
        s = partition(l,r) # 피벗을 기준으로 왼쪽, 오른쪽을 나누는 가운데 위치 구하기
        qsort(l, s-1)      # 왼쪽 퀵 정렬
        qsort(s+1, r)      # 오른쪽 퀵정렬


#A = [7,2,5,3,4,5]
A = [11, 45, 23, 81, 28, 34]
N = len(A)
qsort(0, N-1)
print(A)