'''
빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.
'''
r, g, b = map(int, input().split())
total = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            total += 1
print(total)