n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
result = 0

for i in range(n -1, -1, -1):
    result += (k // coins[i])   # 큰건 몫이 0이라 더해줘도 괜찮음 ^.^
    k %= coins[i]

print(result)