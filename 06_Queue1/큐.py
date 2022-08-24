N =3
q = [0] * N
front = rear = -1

rear += 1   # enqueue(10)
q[rear] = 10

rear += 1   # enqueue(10)
q[rear] = 20

rear += 1   # enqueue(10)
q[rear] = 30

front += 1  # dequeue() 데이터를 지운것은 아니지만 사용x
print(q[front])

front += 1  # dequeue() 데이터를 지운것은 아니지만 사용x
print(q[front])

front += 1  # dequeue() 데이터를 지운것은 아니지만 사용x
print(q[front])
