'''
바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.
'''
check = [list(map(int, input().split())) for _ in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x):