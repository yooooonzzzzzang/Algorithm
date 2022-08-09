import sys
sys.stdin = open("input.txt")

t = 10
for tc in range(1, t+1):
    num = int(input())

    building_list = list(map(int, input().split()))

    view_good = 0


    print(f'#{tc} {building_list}')