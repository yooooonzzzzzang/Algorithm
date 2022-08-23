def permutations(arr):
    # 뽑고 싶은 만큼 뽑았다면 출력 및 종료
    if len(arr) == length:
        print(arr)
        return

    for i in range(len(numbers)):
        if not visited[i]:
            # 1) i번째 원소를 뽑는다.
            visited[i] = True
            arr.append(numbers[i])

            # 2) 재귀함수 진행
            permutations(arr)

            # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
            visited[i] = False
            arr.pop()


numbers = [1, 2, 3, 4]
visited = [False] * len(numbers)
length = 3  # 뽑고 싶은 원소의 개수

permutations([])