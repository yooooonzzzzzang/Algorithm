
l = [1,9,8,7,6,5,4,3,2,1]
n = len(l)
for j in range(n):
    for i in range(1, n-j):
        if l[i-1] >= l[i]:
            l[i-1],l[i] = l[i], l[i-1]

print(l)
for j in range(n):
    for i in range(1, n-j):
        if l[i-1] < l[i]:
            l[i-1],l[i] = l[i], l[i-1]

print(l)