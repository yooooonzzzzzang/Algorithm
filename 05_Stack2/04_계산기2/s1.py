import sys

sys.stdin = open('input (2).txt', encoding='utf-8')

for t in range(1, 10 + 1):
    N = int(input())
    word = input()
    postfix = ''    # 후위표기법 변환 결과
    stack1 = []     # 후위표기법으로 변환할때 연산자저장
    stack2 = []     # 후위표기법 계산할때 피연산자 저장
    result = 0      # 후위표기법 계산 결과

    # 1. 후위표기법으로 변환
    for token in word:
        if token in '*+':
            if not stack1:
                stack1.append(token)
            elif token == '*':
                while stack1 and stack1[-1] == '*':
                    postfix += stack1.pop()
                stack1.append(token)
            elif token == '+':  # '(' 없음
                while stack1:
                    postfix += stack1.pop()
                stack1.append(token)
        else:
            postfix += token
    while stack1:
        postfix += stack1.pop()

    # 2. 후위표기법 계산하기
    for char in postfix:
        if char not in '*+':
            stack2.append(int(char))
        else:
            x2 = stack2.pop()
            x1 = stack2.pop()
            if char == '+':
                stack2.append(x1 + x2)
            elif char == '*':
                stack2.append(x1 * x2)
    result = stack2[-1]
    print(f'#{t} {result}')