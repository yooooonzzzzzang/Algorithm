# def combinations(n,r,s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = arr[i]
#             combinations(n, r-1, i+1)
arr = [1,2,3]
n = len(arr)
temp = []
real = []
for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            temp.append(arr[j])
    real.append(temp)
    temp = []

print(real)
for i in real:
    if len(i) == 2:
        print(*i)
# r = 2
# comb = [0] * r
# combinations(n,r,0)

















# for i in range(1 << n):
#     for j in range(n):
#         if i & (1<<j):
#             ar.append(j)
#     real.append(ar)
#     ar = []
# print(real)
