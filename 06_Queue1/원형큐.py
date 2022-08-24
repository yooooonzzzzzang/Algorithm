N =3
q = [0] * N
front = rear = 0

rear = (rear + 1) % N   # enqueue(10)
q[rear] = 10

rear = (rear + 1) % N   # enqueue(20)
q[rear] = 20

rear = (rear + 1) % N   # enqueue(30)
q[rear] = 30

rear = (rear + 1) % N   # enqueue(30)
q[rear] = 40

front = (front + 1) % N  # dequeue() 데이터를 지운것은 아니지만 사용x
print(q[front])

front = (front + 1) % N  # dequeue() 데이터를 지운것은 아니지만 사용x
print(q[front])

front = (front + 1) % N  # dequeue() 데이터를 지운것은 아니지만 사용x
print(q[front])
