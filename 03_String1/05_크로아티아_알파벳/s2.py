word = input()
cro_char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for i in cro_char:
    count += word.count(i)
    word = word.replace(i,"")


count += len(word)
print(count)