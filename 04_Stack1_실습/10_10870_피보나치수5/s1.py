#  Fn = Fn-1 + Fn-2 (n ≥ 2)

def pibo(n):
    # 종료 조건
    if n <= 1:
        return n
    # 점화식 (재귀식)
    return pibo(n-2)+pibo(n-1)


N = int(input())

print(pibo(N))