import sys

sys.stdin = open('input.txt', encoding='utf-8')
'''
도착점에서 반대로 출발하기
1. 도착점 찾기
2. 델타로 움직이며 1로 위치 이동하기 
3. 언제까지? x (행)가 0 일때까지
'''
for t in range(1, 10 + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 좌 우 상 (아래는 고려하지 않음)
    dx, dy = [0, 0, -1], [-1, 1, 0]

    # 도착지점을 현재위치로 설정
    for x in range(100):
        for y in range(100):
            if ladder[x][y] == 2:
                current_x = x
                current_y = y

    # 델타검색을 하면서 1이 있으면 현재위치 이동 - x 가 0 일때까지
    while current_x > 0:
        for i in range(3):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]
            # 범위 확인 & 사다리 다음 위치가 1 인지
            if 0 <= next_x < 100 and 0 <= next_y < 100 and ladder[next_x][next_y] == 1:
                ladder[current_x][current_y] = 0 # 전에 왔던 길 0 으로 바꿔줘서 돌아가지 못하게 해야함
                current_x, current_y = next_x, next_y

    print(f'#{tc} {current_y}')