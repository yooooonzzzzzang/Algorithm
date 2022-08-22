import sys

sys.stdin = open('sample_input.txt')
'''
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
'''
for t in range(1, int(input()) + 1):
    result = 0
    brackets = input()
    stack = []

    for bracket in brackets:
        if bracket != "(" and bracket != "{" and bracket != ")" and bracket != "}":     # 괄호가 아닐때
            continue
        else:
            if not stack and (bracket ==')' or bracket =='}'):  # stack이 비었고 } or ) 나왔을때 result = 0  으로 종료
                result = 0
                break
            if bracket == '(' or bracket == '{':      # (, { 일때만 저장
                stack.append(bracket)
            elif stack[-1] == '{' and bracket == '}':   # {} 짝맞추기
                stack.pop()
            elif stack[-1] == '(' and bracket == ')':   # () 짝맞추기
                stack.pop()
            else:            # 그 외는 올바르지 않음        ex)   ( } )
                break
    else:   # 다 pop 되고 비었을때 정상
        if not stack:
            result = 1

    print(f'#{t} {result}')