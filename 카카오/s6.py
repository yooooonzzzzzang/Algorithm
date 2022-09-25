def solution(n, m, x, y, r, c, k):
    answer = ''
    dx = [-1, 1, 0, 0]
    dy = [0, 0,-1,1]
    myth = [['.'] * m for _ in range(n)]
    myth[x-1][y-1] = 's'
    myth[r-1][c-1] = 'e'
    for i in range(n):
        for j in range(m):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx< n and 0<= ny< n :
                    if myth[nx][ny] == 'e':

    print(myth)
    return answer



ar1 = [3, 4, 2, 3, 3, 1, 5]
print(solution(*ar1))