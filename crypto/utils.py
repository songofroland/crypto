from itertools import count, islice

from math import gcd, sqrt


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
