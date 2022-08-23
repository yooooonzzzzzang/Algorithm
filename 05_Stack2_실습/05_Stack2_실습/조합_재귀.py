def combinations(arr, depth):
    # 전체 원소의 개수만큼 재귀가 진행됐다면 종료
    if depth == len(numbers):
        # 뽑고 싶은 만큼 뽑았다면 출력
        if len(arr) == length:
            print(arr)
        return

    # 1) 현재 원소를 뽑고 다음 재귀로 진행하는 경우
    combinations(arr + [numbers[depth]], depth + 1)

    # 2) 현재 원소를 뽑지 않고 다음 재귀로 진행하는 경우
    combinations(arr, depth + 1)


numbers = [1, 2, 3, 4]
length = 3  # 뽑고 싶은 원소의 개수

combinations([], 0)