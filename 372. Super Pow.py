def superPow(a, b):
    res = 1
    for i in b:
        res = pow(res, 10) * pow(a, i) % 1337
    return res
