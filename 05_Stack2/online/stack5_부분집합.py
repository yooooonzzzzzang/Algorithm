def f(i, N):
    if i == N :
        print(bit)
    else:
        bit[i] = 1      # A[i] 가 부분집합에 포함
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)


A = [1,2,3]
bit = [0] * 3
f(0,3)