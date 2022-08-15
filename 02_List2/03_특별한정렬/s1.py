import sys

sys.stdin = open('sample_input.txt')
'''
1. 리스트 arr 을  정렬한다. 
2. 오름차순 리스트에 arr [0]~[4] 를 담는다
3. 내림차순 리스트에 arr [N-1]~ [N-5] 를 담는다 
4. 새로운 리스트의 홀수 인덱스에 내림차순 리스트,
                  짝수 인덱스에 오름차순 리스트를 담는다 
'''
for t in range(1, int(input()) + 1):
    N = int(input())    # 정수의 개수
    arr = list(map(int, input().split()))
    arr_sort = []   # 오름차 5개 저장할 인덱스
    arr_reverse_sort =[]    # 내림차 5개 저장할 인덱스
    final_list = []
    # 정렬(오름차) [1, 2, 3, .. ] - 버블정렬 이용
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # 오름차 5개 저장
    for i in range(5):
        arr_sort += [arr[i]]

    # 내림차 5개 저장
    for i in range(N-1, N-5-1, -1):
        arr_reverse_sort += [arr[i]]

    #
    for i in range(10): # 0 ~ 9
        if i % 2 == 0:  # 짝수 - 내림차
            final_list += [arr_reverse_sort[i//2]]
        else:   # 홀수 - 오름차
            final_list += [arr_sort[i//2]]
    print(f'#{t}', *final_list)
