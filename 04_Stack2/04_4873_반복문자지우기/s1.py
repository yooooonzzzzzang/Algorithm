import sys

sys.stdin = open('sample_input.txt')
# 스택의 push 와 pop 이용!
for t in range(1, int(input()) + 1):
    result = 0
    arr = input()
    stack = []
    top = -1
    for char in arr :
        if top == -1:        # 처음에는 비교 못하고 append
            stack.append(char)
            top += 1
            continue
        if stack[top] != char:     # 스택의 top 과 다르면 삽입
            stack.append(char)
            top += 1
        else:                       # 같으면 top 값 제거
            stack.pop()
            top -= 1

    result = stack
    print(f'#{t} {len(result)}')