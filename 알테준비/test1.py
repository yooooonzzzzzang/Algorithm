def solution(n, m):
    answer = []
    arr = []

    max_n = max(n, m)

    for i in range(1, max_n):
        if n % i == 0 and m % i == 0:
            arr.append(i)
    answer.append(max(arr))

    return [max(arr), n * m // max(arr)]

n = 4
m = 8
print(solution(n,m))