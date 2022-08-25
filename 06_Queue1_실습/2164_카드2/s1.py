# 덱으로 풀면 통과
from collections import deque

n = int(input())
queue = deque(range(1, n + 1))
print(queue)
while len(queue) > 1:
    queue.popleft()
    print(queue)
    queue.append(queue.popleft())

print(queue[0])