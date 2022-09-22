# 16진수 문자 ->2진수->7개씩 끊어서 10 진수로 변환
'''
2
0F97A3
01D06079861D79F99F
'''
for t in range(1, int(input()) + 1):
    arr = input()
    print(int(arr,16))
