'''
l = [1,9,8,7,6,5,4,3,2,1]

for j in range(len(l)):
    k = len(l) - j
    for i in range(1, k):
        if l[i-1] >= l[i]:
            temp = l[i-1]
            l[i-1] = l[i]
            l[i] = temp

'''


def sort_arr(li):

    return
def sort_reverse(li):

    return
a = [5, 1, 35, 8]
print(sort_arr(a))
print(sort_reverse(a))
