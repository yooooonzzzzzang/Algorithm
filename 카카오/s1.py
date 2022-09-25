from datetime import datetime, timedelta



def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today,'%Y.%m.%d')
    info = {}
    for idx, i in enumerate(privacies):
        date, grade = i.split()
        month = 0
        if grade == 'A':
            month = 6
        elif grade == 'B':
            month = 12
        elif grade == 'C':
            month = 3
        elif grade == 'Z':
            month = 3
        elif grade =='D':
            month = 5
        date = datetime.strptime(date,'%Y.%m.%d')
        info[idx] = [date,grade, month*28]
    print(info)
    for i in range(len(privacies)):
        nowdays = today.year*12*28+today.month*28+today.day
        contractdays = info[i][0].year*12*28+info[i][0].month*28+info[i][0].day+info[i][2]
        print(nowdays)
        print(contractdays)
        if nowdays >= contractdays != 0:
            answer.append(i+1)


    return answer



today ="2022.05.19"
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
terms = ["A 6", "B 12", "C 3"]

print(solution(today, terms, privacies))