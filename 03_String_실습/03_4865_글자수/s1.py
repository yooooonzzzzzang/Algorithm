import sys

sys.stdin = open('sample_input.txt')
'''
문자열은 iterable 이라는 것과 최대값 구하기를 이용
'''
for t in range(1, int(input()) + 1):
    result = 0
    str1 = input()
    str2 = input()
    for i in str1:
        if result < str2.count(i):  # 최대값 구하는 방법과 같음
            result = str2.count(i)
    print(f'#{t} {result}')