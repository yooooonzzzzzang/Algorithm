# 퀵정렬 - 1) 호어 방식

def partition(arr, left, right):
    pivot = arr[left]  # 가장 왼쪽 원소를 피벗으로 지정
    i, j = left, right

    while i <= j:
        # 1. 피벗보다 큰 값이 나올 때까지 i + 1
        while i <= j and arr[i] <= pivot:
            i += 1

        # 2. 피벗보다 작은 값이 나올 때까지 j - 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        # 3. 피벗보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]  # i > j가 되면 피벗과 j 위치 원소 교환 (피벗을 가운데로 옮기는 작업)

    return j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)  # 피벗을 기준으로 왼쪽, 오른쪽을 나누는 가운데 위치 구하기
        quick_sort(arr, left, middle - 1)  # 왼쪽 퀵정렬
        quick_sort(arr, middle + 1, right)  # 오른쪽 퀵정렬


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)