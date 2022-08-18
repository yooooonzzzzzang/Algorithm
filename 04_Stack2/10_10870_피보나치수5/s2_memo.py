
def pibo(n):
    if len(memo) <= n:
        memo.append(pibo(n - 1) + pibo(n - 2))
    return memo[n]



memo = [0,1]
print(pibo(5))