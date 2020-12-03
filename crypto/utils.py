from itertools import count, islice

from math import gcd, sqrt

from math import gcd


def next_prime(offset: int = 0) -> int:
    if (not offset & 1) and (offset != 2):
        offset += 1
    if is_prime(offset):
        offset += 2
    while True:
        if is_prime(offset):
            break
        offset += 2
    return offset


def get_primitive_root(modulo: int) -> int:
    required_set = {num for num in range(1, modulo) if gcd(num, modulo)}
    for g in range(1, modulo):
        if required_set == {pow(g, powers, modulo) for powers in range(1, modulo)}:
            return g


def is_prime(num: int) -> bool:
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num - 1, num) == 1


def get_smallest_co_prime(M: int) -> int:
    for i in range(2, M):
        if gcd(i, M) == 1:
            return i


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def get_modular_inverse(a: int, m: int) -> int:
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


def PI(vals):
    accum = 1
    for v in vals:
        accum *= v
    return accum


# TODO: Make it by myself
def lagrange_interpolate(x, p, x_s, y_s):
    k = len(x_s)
    nums = []
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([divmod(nums[i] * den * y_s[i] % p, dens[i], p) for i in range(k)])
    return (divmod(num, den, p) + p) % p


def divmod(num, den, p):
    inv, _ = extended_gcd(den, p)
    return num * inv


def extended_gcd(a, b):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y