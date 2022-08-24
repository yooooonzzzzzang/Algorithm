N = int(input())
q = [i+1 for i in range(N)]
discard = []
while len(q) > 1:
    discard.append(q.pop(0))
    q.append(q.pop(0))

print(*discard, *q)