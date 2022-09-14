'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre(n):
    if n:   # n != 0
        print(n, end=" ")        # V
        pre(ch1[n])     # L
        pre(ch2[n])     # R

V = int(input())    # 정점의 개수
arr = list(map(int, input().split()))

E = V-1     # 간선의 수
# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

pre(1)