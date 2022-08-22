import sys
sys.stdin = open("sample_input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    number = input()    # 0으로 시작할 수 있어 str로 받는다
    numbers = [0] * 10    # 0~9까지 숫자의 개수를 담을 리스트

    for num in number:
        numbers[int(num)] += 1  # 리스트 numbers에 0~9 숫자 카운팅해줌

    card = 0    # 가장 많이 나온 숫자 0으로 초기화
    card_count = numbers[0] # 가장 많이 나온 숫자 개수 numbers[0]으로 초기화
    for i in range(1, len(numbers)):    # 1부터 (numbers[0]은 이미 card_count임) numbers 길이
        if numbers[i] >= card_count:    # count 가 같을때 큰 수로 바꿔줘야하기때문에 >= 로 조건 줌
            card_count = numbers[i]     # card_count 변경
            card = i                    # card 변경
    print(f'#{tc} {card} {card_count}')




