import sys

sys.stdin = open('input.txt')

for t in range(1, 10 + 1):
    stack = []
    N, numbers = input().split()
    for num in numbers:
        if not stack or stack[-1] != num:   # 처음 시작하거나 (if stack == [])
            stack.append(num)               # stack 의 top번째 = [-1] 번째와 num 이 다르면 push
        else:
            stack.pop()                     # 아니면 stack[-1] = None -> pop

    print(f'#{t}',''.join(stack))   # fprint에서는 언패킹이 안되는 것같다.
                                    # 밖에서 언패킹을 했는데 1 2 3 중간에 공백이 들어가서 조인사용