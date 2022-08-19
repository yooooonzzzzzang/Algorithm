import sys
import re
sys.stdin = open('s_input.txt')

for t in range(1, int(input()) + 1):

    N = int(input())
    sentence = input()
    result = []
    new2 = []
    new = re.split('[?,!,.]', sentence)     # 마지막에 공백까지 들어감 len(new)-1

    for i in range(len(new)-1):
        new2 = new[i].split()
        count = 0
        for j in range(len(new2)):
            if new2[j][0].isupper() and new2[j][-1].islower():
                count +=1

        result.append(count)
    print(f'#{t}', *result)
