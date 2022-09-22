# N 개 중 R 개를 고르는 순열
def f(i,k,r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:    # a[j] 가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 가 사용됨으로 표시
                p[i] = a[j]     # p[i]는 a[j]로 결정
                f(i+1, k, r)       # p[i+1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 5
R = 3
a =[i for i in range(1,N+1)]
used = [0] * N
p = [0] * R    # 실제 저장할 공간
f(0,N,R)