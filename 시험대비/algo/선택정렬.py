# 주어진 리스트에서 최소값을 맨 앞에 값과 교환, 반복
def select_sort(a, n):
    for i in range(n-1):    # 0,1,2,,,, n-2   - 미정렬원소가 하나 남으면 마지막 원소가 가장 큰 값
        minIdx = i
        for j in range(i+1, N): # i+1, .. n-1    - 바꿀 맨 앞자리 남기고 다음부터 최소값 찾음
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
    return a


arr = [2,1,7,0]
N = len(arr)
print(select_sort(arr, N))
