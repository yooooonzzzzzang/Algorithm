'''
바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
'''
d=[]
for i in range(20) :
    d.append([])
    for j in range(20) :
        d[i].append(0)

for i in range(19) :
    a = input().split()
    for j in range(19) :
        d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
    x,y=input().split()
    x=int(x)
    y=int(y)
    for j in range(1, 20) :
        if d[j][y]==0 :
            d[j][y]=1
        else :
            d[j][y]=0

        if d[x][j]==0 :
            d[x][j]=1
        else : d[x][j]=0

for i in range(1, 20) :
    for j in range(1, 20) :
        print(d[i][j], end=' ')
    print()