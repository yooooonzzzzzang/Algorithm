#  솔루션 코드를 작성합니다.
import sys

sys.stdin = open('input.txt')


def palindrome(words):
    for m in range(100, 0, -1):             # 길이가 100부터 시작해서 점차 길이를 줄여가며 회문 판별
        for i in range(100):                # 가로 검사
            for j in range(100 - m + 1):    # 인덱스 범위 초과 방지
                word = ''                   # 검사할 부분 문자열 공백으로 초기화
                for k in range(j, j + m):   # 현재 행의 j ~ j+m-1 범위 문자를 word에 붙여주기
                    word += words[i][k]
                if word == word[::-1]:      # 회문이면
                    return len(word)        # 길이 반환
        for j in range(100):                # 세로 검사
            for i in range(100 - m + 1):
                word = ''
                for k in range(i, i + m):   # 현재 열의 i ~ i+m-1 범위 문자를 word에 붙여주기
                    word += words[k][j]
                if word == word[::-1]:
                    return len(word)


for _ in range(10):
    tc = int(input())
    arr = [list(map(str, input())) for _ in range(100)]

    print(f'#{tc} {palindrome(arr)}')