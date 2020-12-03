from random import randrange

from utils import next_prime, lagrange_interpolate


class TrivialSecretGenerator:
    def __init__(self, s: int = next_prime(999), n: int = 99, k: int = 9999):
        self.n = n
        self.k = k
        self.secret = s
        self.random_values = [randrange(0, self.k) for _ in range(self.n)]

    def restore_secret(self, chunks: list) -> int:
        return sum(chunks) % self.k

    def secret_to_chunks(self) -> list:
        chunks = []
        for i in range(self.n):
            s = self.secret
            for j in range(i):
                s -= chunks[j]
            s %= self.k
            chunks.append(s)
        return chunks


class ShamirSecretGenerator:
    def __init__(self, s: int = next_prime(999), n: int = 999, t: int = 99):
        self.secret = s
        self.n = n
        self.t = t
        self.p = self._get_fitting_p()
        self.a_numbers = [randrange(999999999) for _ in range(1, self.t)]

    def _get_fitting_p(self):
        p = next_prime(3000)
        while p < self.secret or p < self.n:
            p = next_prime(p)
        return p

    def _generate_key(self, x: int):
        total = self.secret
        for j in range(1, self.t):
            total += self.a_numbers[j - 1] * pow(x, j)
        return total % self.p

    def secret_to_chunks(self) -> list:
        return [(i, self._generate_key(i)) for i in range(1, self.n + 1)]

    def restore_secret(self, chunks: list) -> int:
        return lagrange_interpolate(0, self.p, *zip(*chunks[: self.t]))


trivial_gen = TrivialSecretGenerator()
trivials = trivial_gen.secret_to_chunks()
assert trivial_gen.secret == trivial_gen.restore_secret(
    trivials
), "Trivial secret not restored correctly."

shamir_gen = ShamirSecretGenerator()
shamirs = shamir_gen.secret_to_chunks()
assert shamir_gen.secret == shamir_gen.restore_secret(
    shamirs
), "Shamir secret not restored correctly."
