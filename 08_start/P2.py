

for t in range(1, int(input()) + 1):
    arr = input()
    for i in range(0, len(arr), 7):
        print(int(arr[i:i+7],16))