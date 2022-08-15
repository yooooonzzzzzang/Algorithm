import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')
'''
1. for 문을 돌면서 x1, y1, x2, y2, color 를 입력받고
2. 해당 위치에 색깔들을 더해줌
3. 보라색은 1+2 가 합한 3이되므로 3인 것을 세어준다.

'''
for t in range(1, int(input()) + 1):
    square = [[0] * 10 for _ in range(10)]
    square_num = int(input())
    for i in range(square_num): # square_num 번 만큼 입력받기
        x1, y1, x2, y2, color = map(int,input().split())

        for x in range(x1, x2+1):   # 색깔 더해주기
            for y in range(y1, y2+1):
                square[x][y] += color
    total = 0
    for i in range(10):    # square 에 3이 있으면 카운트
        for j in range(10):
            if square[i][j] == 3:
                total += 1

    print(f'#{t} {total}')

