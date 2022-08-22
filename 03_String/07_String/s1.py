import sys

sys.stdin = open('input.txt', encoding="utf-8")
for i in range(1, 11):
    tc = int(input())
    find_str = input()
    arr = input()

    print(f'#{tc} {arr.count(find_str)}')
