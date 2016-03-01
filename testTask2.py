i = 758965444


def to_st(k):
    list_num = []
    if k < 0 or k >= 1000000000:
        print('ERROR! 0 <= n < 1000000000')
        quit()
    while k != 0:
        k, r = divmod(k, 10)
        list_num.insert(0, r)
    if len(list_num) > 3:
        list_num.insert(-3, ',')
    if len(list_num) > 7:
        list_num.insert(-7, ',')
    return list_num
result = to_st(i)
print(''.join(map(str, result)))