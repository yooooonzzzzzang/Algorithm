import sys
sys.stdin = open("input.txt")

t = 10
for tc in range(1, t+1):
    num = int(input())

    building_list = list(map(int, input().split()))

    view_good = 0   # 조망권이 좋은 세대 수

    for i in range(2, num-2):   # [2] 부터 [num-3]까지 ex) num = 100인 경우 [2] ~ [97]  인덱스는 0~99까지 있으니까)
        max_num = 0
        for j in range(i-2, i+3):   # [i-2] 부터 [i-2] 까지 돌리면서 최대값을 구함
            if j == i:  # 비교할 [i] 인 경우에는 제외
                continue
            if building_list[j] > max_num:  # 최대값 구하기
                max_num = building_list[j]

        if max_num < building_list[i]:  # [i] 가 주변 아파트 보다 높아야하기때문에
            view_good += (building_list[i] - max_num)   # [i] 와 max 의 차이가 뷰가 좋은 곳

    print(f'#{tc} {view_good}')