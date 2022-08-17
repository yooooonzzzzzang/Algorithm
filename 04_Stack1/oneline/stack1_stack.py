stackSize = 10
stack = [0] * stackSize
top = -1    # 초기

top += 1    # push(1)
stack[top] = 1

top += 1    # push(2)
stack[top] = 2

top -= 1    # pop
temp = stack[top + 1]
print(temp)

temp = stack[top]   # pop
top -= 1
print(temp)

stack2 = []     # 다른 방법 pop
stack2.append(10)
stack2.append(20)
print(stack2.pop())
print(stack2.pop())
