def solution(s):

    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, j in enumerate(nums):
        s = s.replace(j, str(i))
    answer = int(s)
    return answer


print(solution("1zerotwozero3"))