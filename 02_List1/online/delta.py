di = [0, 1, -0, -1] # 행의 변화값  오, 아래, 왼, 위
dj = [1, 0, -1, 0]  # 열의 변화값
N = 3
M = 4
arr = [[1,2,3,4],[5,6,7,8]]
for i in range(N):
    for j in range(M):  # 모든 좌표에 대해서 델타이동하겠다.
        #for d in range(1,3) 두칸씩
        for k in range(4):
            ni = i + di[k]  # *d
            nj = j + dj[k]  # *d
            if 0<=ni<N and 0<=nj<M: # 범위를 벗어나지 않으면 이동 (0,0) 등 왼쪽이나 위쪽이 없음
                print(ni, nj)