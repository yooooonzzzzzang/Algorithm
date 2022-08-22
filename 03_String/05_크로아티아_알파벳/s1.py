word = input()
cro_char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_char:
    word = word.replace(i, ".")

print(len(word))