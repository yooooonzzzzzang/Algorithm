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
    current_x = current_y = 0

    # 도착지점을 현재위치로 설정
    for x in range(100):
        for y in range(100):
            if ladder[x][y] == 2:
                current_x = x
                current_y = y
    # 델타검색을 하면서 1이 있으면 현재위치 이동 - x 가 0 일때까지
    print('#', tc)
    print(current_x)
    print(current_y)