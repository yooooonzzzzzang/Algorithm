'''
영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
'''

n = ord(input())
a = ord('a')

for i in range(a, n+1):
    print(chr(i))
