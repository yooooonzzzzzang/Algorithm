# 퀵정렬 - 2) 로무토 방식

def partition(arr, left, right):
    pivot = arr[right]  # 가장 오른쪽 원소를 피벗으로 지정
    i, j = left - 1, left

    while j < right:
        if pivot > arr[j]:
            i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)