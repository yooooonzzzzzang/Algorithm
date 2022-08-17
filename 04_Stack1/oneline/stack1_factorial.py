def f(n):   # 팩토리얼 n! 1! = 1             cf)  0! = 1
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

for i in range(21):
    print(i, f(i))
