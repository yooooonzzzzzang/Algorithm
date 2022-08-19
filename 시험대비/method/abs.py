# 함수로 구현
def abs_sign(number):
    if number >= 0:
        return number
    else:
        return -number


n = int(input())

# if 문으로 구현
if n < 0:
    k = -n
else:
    k = n
print(k)