'''
정점 번호 1 ~ (E + 1)
간선 수
부모- 자식 순
- 3을 루트로 하는 서브트리에 속한 정점의 개수는?

13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0: # 부모가 없으면 root
            return i

def f(n):    #global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0:  # 서브트리가 비어있으면
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1

E = int(input())
arr = list(map(int, input().split()))
V = E + 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 자식이 없으면
        ch1[p] = c  # 자식1로 저장
    else:
        ch2[p] = c
    par[c] = p
root = find_root(V)

print(f(3))

