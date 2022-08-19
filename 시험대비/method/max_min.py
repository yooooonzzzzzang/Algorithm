def max_num(li):
    x = 0
    for i in li:
        if x < i:
            x = i
    return x

def min_num(li):
    x = li[0]
    for i in li:
        if x > i:
            x = i
    return x


a = [1, 2, 6, 9, 12, 54, 60, 32]
print(max_num(a))
print(min_num(a))