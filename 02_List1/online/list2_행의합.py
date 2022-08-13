'''
각 행의 합을 구하고 그 중 최대값을 출력하시오..
3
1 2 3
4 5 6
7 8 9
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
maxV = 0    # 최대 행의 합
for i in range(N):
    rs = 0  # 행의 합
    for j in range(N):  # i 행의 j 열에 접근
        rs += arr[i][j]
    if maxV < rs:
        maxV = rs
print(maxV)