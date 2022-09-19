def solution(seoul):
    for i, j in enumerate(seoul):
        if j == 'Kim':
            index = i
            break

    answer = '김서방은 '+str(index)+'에 있다'
    return answer

# ["Jane", "Kim"]
seoul = ["Jane", "Kim"]
print(solution(seoul))