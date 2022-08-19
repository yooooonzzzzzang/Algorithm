import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    result = []
    N, K = map(int, input().split())    # 수강생의 수. 과제제출한 사람의 수
    submit = list(map(int, input().split()))
    students = list(range(1, N+1))

    for i in students:
        if i not in submit:
            result.append(i)

    print(f'#{t}', *result)
