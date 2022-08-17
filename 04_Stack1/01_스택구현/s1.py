def push(item):     # 스택 삽입 함수
    global top
    global size
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item
        print(stack[top])

def pop():     # 스택 제거 함수
    if len(stack) == 0:
        print('underflow')
        return
    else:
        return stack.pop(-1)    # 가장 마지막 값 , 후입선출


size = 3
stack = [0] * size
top = -1

push(10)
push(20)
push(30)
print(pop())
print(pop())
print(pop())






