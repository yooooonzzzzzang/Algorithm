import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())   # K: 충전시 이동가능 한 정류장 수, N: 총 정류장, ,M: 충전기 설치된 정류장의 수
    charger = list(map(int, input().split()))    # 충전소 위치를 담은 리스트
    bus = 0  # 버스 위치
    charger_count = 0   # 충전 횟수
    while bus + K < N:
        for i in range(K, 0, -1):  # K 범위에서 이동, range(k) 로 할경우 i = 0만 반복함
            if bus + i in charger:  # 버스가 이동한 위치에 충전소가 있다면
                bus += i    # 위치변경
                charger_count += 1
                break   # for 종료
        else:   # 마지막 정류장에 도착하지 못하면
            charger_count = 0
            break
    print(f'#{t} {charger_count}')
