'''
출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.
'''
n = int(input())
arr = list(map(int, input().split()))
student = [0]*23
for i in range(n):
    student[arr[i]-1] += 1
print(*student)