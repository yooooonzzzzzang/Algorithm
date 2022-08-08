import sys
sys.stdin = open("input.txt")

t = 10
for tc in range(1, t+1):
    num = int(input())
    building_list = list(map(int, input().split()))
    result = 0
    for i in building_list:
        if building_list[i+1]- building_list[i] >= 2:
            result += 1
    print(f'#{tc} {result}')