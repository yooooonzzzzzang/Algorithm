n = int(input())
arr = [0] * 1001
max_height = 0  # 최대 높이
max_height_index = 0  # 최대 높이의 인덱스
end_index = 0  # 끝 인덱스
for _ in range(n):
    w, h = map(int,input().split())
    arr[w] = h
    if max_height < h:
        max_height = h
        max_height_index = w
    end_index = max(end_index, w)

stack = []
result = 0
for i in range(0, max_height_index + 1):
    if not stack:
        stack.append(arr[i])
    else:
        if stack[-1] < arr[i]:
            stack.pop()
            stack.append(arr[i])
    result += stack[-1]

stack = []
for j in range(end_index, max_height_index, -1)