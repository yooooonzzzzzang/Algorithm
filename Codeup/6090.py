'''
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,
n번째 수를 출력하는 프로그램을 만들어보자.
'''
a, m, d, n = map(int,input().split())
temp = a
for i in range(0, n-1):
    temp = temp * m + d
print(temp)