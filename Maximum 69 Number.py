def maximum69Number (num):
    num = str(num)
    for i in num:
        if i == 6:
            i = 9
    return int(num)
