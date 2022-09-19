'''
input
2
00000010001101
0000000111100000011000000111100110000110000111100111100111111001100111
'''

for t in range(1, int(input()) + 1):
    bins = input()
    for i in range(0,len(bins),7):
        print(int(bins[i:i+7], 2), end=" ")
    print()

