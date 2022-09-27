# 퀵정렬 - 3) 파이썬스러운 방식 but 메모리 더 많이 씀

def quick_sort(arr):
    # 더 이상 분할할 수 없는 경우(종료 조건)
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 가장 왼쪽 원소를 피벗으로 지정
    arr = arr[1:]  # 피벗 제외하여 새로운 리스트 생성

    left_arr = [i for i in arr if i <= pivot]  # 피벗보다 작거나 같은 원소는 왼쪽으로 분할
    right_arr = [j for j in arr if j > pivot]  # 피벗보다 큰 원소는 오른쪽으로 분할

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
print(quick_sort(numbers))