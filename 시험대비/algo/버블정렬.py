
def bubble_sort(a, n):
    for i in range(n-1, 0, -1):     # 이게 중요!!! 점점 작아지는거
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


arr = [2,1,35,7,36,3]
N = len(arr)

print(bubble_sort(arr, N))