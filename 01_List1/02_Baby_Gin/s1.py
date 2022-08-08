import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t+1):
    num = input()   # int(input())시 첫글자가 0 이면 0을 인식을 안함
    c = [0] * 10    # 0~9까지 숫자의 개수를 담을 리스트

    for n in num:  # 리스트 c에 num 각각 개수 넣어주기
       c[int(n)] += 1

    i = 0
    tri = run = 0
    while i < 10:
        if c[i] >= 3:   #triple 확인하기
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: #run 확인하기
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1
    if run + tri == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


