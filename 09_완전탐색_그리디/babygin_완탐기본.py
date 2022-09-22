def baby_gin(n):
    global answer
    triplet = 0
    run = 0
    if n == len(arr):
        if arr[0] == arr[1] == arr[2]:
            triplet += 1
        if arr[2] == arr[1] + 1 == arr[0] + 2:
            run += 1
        if arr[3] == arr[4] == arr[5]:
            triplet += 1
        if arr[5] == arr[4] + 1 == arr[3] + 2:
            run += 1
        if run + triplet == 2:
            answer = True
            return answer
    else:
        for i in range(n, len(arr)):
            arr[n], arr[i] = arr[i], arr[n]
            baby_gin(n + 1)
            arr[n], arr[i] = arr[i], arr[n]


t = int(input())

for tc in range(1, t + 1):
    arr = list(map(int, input()))

    answer = False
    baby_gin(0)
    print(f'#{tc} {answer}')