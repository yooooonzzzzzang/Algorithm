
# # itertools 모듈 이용하기
# from itertools import permutations
#
# numbers = [1, 2, 3, 4]
# length = 3  # 뽑고 싶은 원소의 개수
#
# for case in permutations(numbers, length):
#     print(case)

# 자기 길이만큼 순열 뽑기 (뽑기 안됨)
# def f(i):
#     if i == len(p) :      # 인덱스 i == 원소의 개수
#         print(p)
#     else:
#         for j in range(i, len(p)):
#             p[i], p[j] = p[j], p[i]
#             f(i+1)
#             p[i], p[j] = p[j], p[i]
#
# p = [1,2,3,4,5]
# f(0)

#  visited 이용해 순열뽑기 자기가 원하는 개수만큼 순열뽑기
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


numbers = [1, 2, 3]
visited = [False] * len(numbers)
length = 2  # 뽑고 싶은 원소의 개수

permutations([])