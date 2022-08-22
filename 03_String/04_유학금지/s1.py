no = 'CAMBRIDGE'
letter = input()

for i in no:    # 'CAMBRIDGE' 도 가능
    if i in letter: # 생략 가능
        letter = letter.replace(i, "")

print(letter)