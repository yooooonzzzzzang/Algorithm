'''
3
2+3*4/5
1*2/3+2
3-2*5+4/2-2
'''
for t in range(1, int(input()) + 1):
    word = input()  # 중위표기법
    result = ''  # 후위표기법 변환 결과
    stack = []

    for token in word:
        # 토큰이 연산자 혹은 괄호라면
        if token in '*/+-()':
            # 1) 스택이 비어있는 상태이거나 토큰이 여는 괄호라면 push
            if not stack or token == '(':
                stack.append(token)
            # 2) 토큰이 연산자라면 스택 top과 비교하여 우선순위가 높으면 push,
            # 낮으면 더 우선순위가 낮은 연산자를 만날 때까지 pop 하고 결과 값에 담음
            elif token in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(token)  # 이후 스택에 연산자 push
            elif token in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(token)  # 이후 스택에 연산자 push
            # 3) 토큰이 닫는 괄호라면 여는 괄호를 만날 때까지 모두 pop 하고 결과 값에 담음
            elif token == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()  # 남아있는 여는 괄호 버림

        # 토큰이 피연산자라면 그대로 결과 값에 담음
        else:
            result += token

    # 혹시나 스택에 토큰이 남아있다면 모두 결과 값에 담음
    while stack:
        result += stack.pop()

    print(f'#{t} {result}')