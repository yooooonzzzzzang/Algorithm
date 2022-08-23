import sys

sys.stdin = open('input (2).txt', encoding='utf-8')

for tc in range(1, 11):

    N = int(input())
    word = input()
    stack = []
    result = ""

    # 후위 표기식으로 변환
    for token in word:

        # 토큰이 연산자일 때
        if token in "+*":

            # 스택이 비어있다면 토큰 삽입
            if not stack:
                stack.append(token)

            # 토큰이 곱하기라면 우선순위가 낮은 연산자(+)가 나올 때까지 스택의 마지막 값을 result로 이동
            # 이후 stack에 곱하기 삽입
            elif token == "*":
                while stack and stack[-1] in "*":
                    result += stack.pop()
                stack.append(token)
            # 토큰이 더하기라면 pop을 통하여 스택의 모든 값을 result로 이동
            # 원래는 "("가 나올 때까지만 이동하지만, 이 문제에서는 괄호를 사용하지 않는다.
            # 이후 stack에 더하기 삽입
            elif token == "+":
                while stack:
                    result += stack.pop()
                stack.append(token)

        # 토큰이 연산자가 아닐 경우 result에 바로 넣어준다.
        else:
            result += token

    # 반복문이 끝난 뒤 스택 안에 연산자가 남아있다면 모두 result로 이동시킨다.
    while stack:
        result += stack.pop()
    # 후위 표기식 완료
    print(result)
    # 계산 진행
    for char in result:

        # char가 연산자가 아니라면 스택에 삽입
        if char not in "+*":
            stack.append(int(char))

        # 연산자라면 스택에서 두 값을 꺼내어 연산 실행 후 계산된 값을 스택에 다시 넣어준다.
        else:
            x = stack.pop()
            y = stack.pop()
            if char == "+":
                stack.append(y + x)
            elif char == "*":
                stack.append(y * x)

    # 스택에 남아있는 마지막 값 출력
    print(f"#{tc} {stack[-1]}")