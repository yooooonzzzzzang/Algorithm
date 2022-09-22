'''
5
123123
124467
333444
444456
123444
'''
'''
4
124783
667767
054060
101123
'''
'''
9
111456
123123
233677
112233
333333
123456
667767
054060
101123
'''
def f(i, k):
    if i == k:
        run = 0
        tri = 0
        if card[0] == card[1] and card[1] == card[2]:
            tri += 1
        if card[0]+1 == card[1] and card[1]+1 == card[2]:
            run += 1
        if card[3] == card[4] and card[4] == card[5]:
            tri += 1
        if card[3] + 1 == card[4] and card[4] + 1 == card[5]:
            run += 1
        if tri + run == 2:
            return 1
        else:
            return 0

    else:
        for j in range(i, k):
            card[i], card[j] = card[j], card[i]
            if f(i+1, k):
                return 1
            card[i], card[j] = card[j], card[i]
        return 0


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input()))
    # 순열 만들기
    ans = f(0, 6)
    if ans:
        print("True")
    else:
        print("False")