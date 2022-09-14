'''
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
'''
n = int(input())    # 흰돌의 개수
check = [[0] * 19 for _ in range(19)]
for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        for k in range(19):
            check[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(check[i][j], end=' ')
    print()
