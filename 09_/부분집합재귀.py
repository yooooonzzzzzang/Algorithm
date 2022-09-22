def f(i,k):
    if i == k:
      #  print(bit)
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)
arr = [3, 6, 7]
n = len(arr)

bit = [0] * n       # bit[i] arr[i] 가 부분집합의 원소인지 표시
f(0, n)