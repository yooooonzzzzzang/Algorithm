import sys

sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    '''
    덤프횟수만큼 돌면서 max 와 min 을 찾고 값을 찾고 
    max-1,min +1 을 해준다. 
    다 돌고 다시 평탄화된 max와 min 을 찾은 다음 빼준다.
    '''
    # 평탄화 작업
    while dump > 0:
        max = min = box[0]
        max_id = min_id = 0 # max, min 값이 몇번째인지 알아야함
        for i in range(len(box)):
            if max <= box[i]:
                max = box[i]
                max_id = i
            elif box[i] < min:
                min = box[i]
                min_id = i
        box[max_id] -= 1
        box[min_id] += 1

        dump -= 1
    # 평탄화 작업이 끝난뒤 max 와 min 구하기
    real_max = real_min = box[0]
    for i in range(len(box)):
        if real_max <= box[i]:
            real_max = box[i]
        elif real_min > box[i]:
            real_min = box[i]


    print(f'#{t} {real_max - real_min}')


