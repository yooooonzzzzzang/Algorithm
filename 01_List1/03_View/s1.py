import sys
sys.stdin = open("input.txt")

t = 10
for tc in range(1, t+1):
    num = int(input())

    building_list = list(map(int, input().split()))

    view_good = 0   # 조망권이 좋은 세대 수

    for i in building_list: # [2] 부터 시작 ^^ 집가서 다시 해보자 ^^ 화이팅~~~~~
        if building_list[i]


    print(f'#{tc} {view_good}')