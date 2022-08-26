import sys

sys.stdin = open('sample_input.txt')
t = int(input())


def check():
    # 오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'o':
                for dir in range(4):
                    nx = i
                    ny = j
                    cnt = 0

                    while 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 'o':
                        cnt += 1
                        nx += dx[dir]
                        ny += dy[dir]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'


for tc in range(1, t + 1):
    n = int(input())
    data = [input() for _ in range(n)]

    print('#%d %s' % (tc, check()))
'''
1. 각 테스트 케이스마다 오목판 상태를 입력받고, check() 함수를 통해 반환받은 문자열을 해당 테스트 케이스 번호와 함께 출력한다.
2. check() 함수의 작업은 아래와 같다.
  - (→, ↓, ↘, ↙) 순으로 방향 dx, dy를 정의한다.
  - 오목판의 한 칸 정보를 하나씩 확인하는데, 만약 해당 칸에 돌이 놓여져있다면('o') 방향을 하나씩 확인하여 돌이 연속으로 5개가 놓여져 있는지 확인한다.
  - 만약 연속으로 놓여진 돌의 개수(cnt)가 5 이상이라면 'YES'를 반환하고, 오목판의 상태를 모두 확인하였음에도 'YES'가 반환되지 않았다면 'NO'를 반환한다.
'''
