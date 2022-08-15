'''
출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
'''
n = int(input())
arr = list(map(int, input().split()))

min = arr[0]
for i in arr:
    if i < min:
        min = i
print(min)
