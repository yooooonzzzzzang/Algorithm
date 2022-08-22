import sys

sys.stdin = open('sample_input (1).txt')

def binary ( key, P):
    l = 1  # 왼쪽 페이지
    r = P  # 오른쪽 페이지
    cnt = 0
    while l <= r:
        c = (l + r) // 2  # 중간 페이지
        cnt += 1
        if c == key:
           return cnt
        elif c > key:
            r = c - 1
        else:
            l = c + 1

for t in range(1, int(input()) + 1):
    P, Pa, Pb = map(int, input().split())

    a_c = binary( Pa, P)
    b_c = binary( Pb, P)

    if a_c < b_c:
        print(f'#{t} A')
    elif a_c > b_c:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')
   