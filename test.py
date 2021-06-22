def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# edit the text below to see how this works
text = 'Cuddly Llamas'
bits = string2bits(text)

ans = sum([int(x, 2) for x in bits])
print(ans)
enc = ans**5 % 35
print(enc)
dec = modinv(enc ** 29, 35)
print(dec)
