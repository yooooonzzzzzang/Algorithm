def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)




for i in range(4):
    print(i, fibo(i))