import sys

sys.stdin = open('input.txt')

for t in range(1, 10 + 1):
    N = int(input())
    word = input()
    postfix = ''    # 후위 표기 법 변환 결과
    stack = []
    # 1. 후위 표기로 변환
    for token in word:
        if token in '*+()':   # 연산자인 경우
            if not stack or token == '(':   # 스택이 비었거나 ( 때
                stack.append(token)
            elif token == '*':
                while stack and stack[-1] == '*':
                    postfix += stack.pop()
                stack.append(token)
            elif token == '+':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()     # 남아있는 여는 괄호도 제거

        else:                   # 피연산자인 경우 결과값에 담음
            postfix += token
    while stack:
        postfix += stack.pop()

    # 2. 후위 표기식 계산
    for char in postfix:
        if char in '*+':
            y = stack.pop()
            x = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '*':
                stack.append(y * x)
        else:
            stack.append(int(char))

    print(f'#{t} {stack[-1]}')