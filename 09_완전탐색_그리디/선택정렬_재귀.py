'''
# 주어진 리스트에서 최소값을 맨 앞에 값과 교환, 반복
def select_sort(a, n):
    for i in range(n-1):    # 0,1,2,,,, n-2   - 미정렬원소가 하나 남으면 마지막 원소가 가장 큰 값
        minIdx = i
        for j in range(i+1, n): # i+1, .. n-1    - 바꿀 맨 앞자리 남기고 다음부터 최소값 찾음
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
        print(a)
    return a

A = [3, 7, 1, 2]
select_sort(A, 4)
'''
def SelectionSort(A,s):                 # A:비교할 값, s:처음 인덱스
    n = len(A)                          # 비교할 값의 길이
    if s == n-1:                        # 비교 끝 - 종료 [n-1: 미정렬원소가 하나 남으면 마지막 원소가 가장 큰 값이라]
        return
    minIdx = s                          # 시작값을 최소값을 나타내는 인덱스로
    # 최소값 구하기
    for i in range(s+1, n):             # s+1 부터 n-1 까지 - 바꿀 맨 앞자리 남기고 다음부터 최소값 찾음
        if A[minIdx] > A[i]:            # A[minIdx] 더 작은 값이 나오면 자리바꾸기
            minIdx = i
    A[s], A[minIdx] = A[minIdx], A[s]   # 최소값과 s 의 위치바꾸기
    SelectionSort(A, s+1)               # 이제 다음 자리로 넘어가기 s+1 ~ n-1 까지


A = [2, 4, 6, 1, 9, 8, 7, 0]
SelectionSort(A, 0)
print(A)
