import random

from math import gcd


class BBSGenerator:
    def __init__(self, prime_offset: int = 1000):
        self.prime_offset = prime_offset

    def rand_string(self, length: int) -> str:
        N = self._get_nearest_blum()
        x = self._get_seed(N) ** 2 % N
        result = [bin(x)[-1]]

        for i in range(length):
            x = x ** 2 % N
            result.append(bin(x)[-1])

        return "".join(result)

    def _get_nearest_blum(self) -> int:
        p = self._get_bbs_prime(self.prime_offset)
        q = self._get_bbs_prime(p + 1)
        return p * q

    def _get_seed(self, blum: int) -> int:
        x = random.randrange(blum)
        while gcd(x, blum) > 1:
            x = random.randrange(blum)
        return x

    def _get_bbs_prime(self, offset: int) -> int:
        num = offset
        while num % 4 != 3 or not self._is_prime(num):
            num += 1
        return num
