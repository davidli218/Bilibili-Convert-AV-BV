table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}
for j in range(58):
    tr[table[j]] = j
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608


def dec(x):
    """
    Convert BVid to Aid
    :param x: Example: BV17x411w7KC
    :return: Example: AV170001
    """
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58 ** i
    return 'AV' + str((r - add) ^ xor)


def enc(x: str):
    """
    Convert Aid to BVid
    :param x: Example: AV170001
    :return: Example: BV17x411w7KC
    """
    x = int(x[2:])
    x = (x ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[x // 58 ** i % 58]
    return ''.join(r)
