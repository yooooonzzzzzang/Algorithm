def itoa(number):
    if number == 0:
        return '0'

    is_positive = True
    if number < 0:      # 음수에 대한 처리
        is_positive = False
        number = -number

    str_number = ''
    while number > 0:
        number, remainder = number // 10, number % 10  # divmod(number, 10)
        str_number = chr(ord('0') + remainder) + str_number

    if not is_positive:
        str_number = '-' + str_number

    return str_number


result = itoa(123)
print(type(result))
print(result)