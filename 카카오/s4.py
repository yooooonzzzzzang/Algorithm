def solution(numbers):
    answer = []

    for i in numbers:
        p = bin(i)
        real = p[2:]
        print(real)
    return answer




num1 = [7,5]
num2 = [63,111,95]
print(solution(num1))
print(solution(num2))