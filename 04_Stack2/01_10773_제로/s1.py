# 숫자들을 계속 list 에 push 하다가 0 이 나올때마다 pop 해
# top 에 있는 숫자를 result 에 저장한다.

stack = []
for _ in range(int(input())):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))