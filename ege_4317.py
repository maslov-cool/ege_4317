def from_ten_to_base(n, base):
    res = ''
    while n != 0:
        res += str(n % base)
        n //= base
    return res[::-1]


def from_base_to_ten(n, base):
    res = 0
    for i in range(len(str(n))):
        res += int(str(n)[::-1][i]) * base ** i
    return str(res)


def transformation(n):
    n5 = from_ten_to_base(n, 5)
    if int(n5[-1]) % 2 == 0:
        n5 += '2'
    else:
        n5 = '2' + n5 + '3'
    return int(from_base_to_ten(n5, 5))

for i in range(9999, 1, -1):
    if transformation(i) < 1000:
        print(i)
        break