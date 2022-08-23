import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    word = list(map(str, input().split()))
    stack = []

    for char in word:
        if char not in '*/+-.':   # 피연산자인 경우
            stack.append(int(char))
        elif char == '.':
            if len(stack) != 1:     # 출력 결과 개수는 한개여야함
                print(f'#{t} error')
                break
            print(f'#{t} {stack.pop()}')
        else:   # 연산자인 경우
            if len(stack) < 2:      # 피연산자가 2개 미만 -> 연살할 피연산자가 부족
                print(f'#{t} error')
                break
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                if x == 0:          # zerodivision
                    print(f'#{t} error')
                    break
                stack.append(y // x)

