def solution(survey, choices):
    answer = ''
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for idx, i in enumerate(survey):
        if choices[idx] == 1:
            dic[str(i[0])] += 3
        elif choices[idx] == 2:
            dic[str(i[0])] += 2
        elif choices[idx] == 3:
            dic[str(i[0])] += 1
        elif choices[idx] == 4:
            pass
        elif choices[idx] == 5:
            dic[str(i[1])] += 1
        elif choices[idx] == 6:
            dic[str(i[1])] += 2
        elif choices[idx] == 7:
            dic[str(i[1])] += 3

    if dic['R'] > dic['T']:
        answer += 'R'
    elif dic['R'] == dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] > dic['F']:
        answer += 'C'
    elif dic['C'] == dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] > dic['M']:
        answer += 'J'
    elif dic['J'] == dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] > dic['N']:
        answer += 'A'
    elif dic['A'] == dic['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

print(solution(survey,choices))