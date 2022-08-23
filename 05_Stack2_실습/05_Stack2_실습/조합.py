def combinations(arr, start):
    # 뽑고 싶은 만큼 뽑았다면 출력 및 종료
    if len(arr) == length:
        print(arr)
        return

    for i in range(start, len(numbers)):
        # 1) i번째 원소를 뽑는다.
        arr.append(numbers[i])

        # 2) 재귀함수 진행
        combinations(arr, i + 1)    # 내가 다음에 뽑을 숫자는 지금보다 커야한다 - 조합은 순서가 상관없기때문에

        # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
        arr.pop()


numbers = [1, 2, 3, 4]
length = 3  # 뽑고 싶은 원소의 개수

combinations([], 0)