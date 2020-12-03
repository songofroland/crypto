from random import randrange

from utils import next_prime, lagrange_interpolate


class TrivialSecretGenerator:
    def __init__(self, s: int = next_prime(999), n: int = 99, k: int = 9999):
        self.n = n
        self.k = k
        self.s = s
        self.random_values = [randrange(0, self.k) for _ in range(self.n)]
        

    def secret_to_chunks(self) -> list:
        chunks = []
        for i in range(self.n):
            s = self.s
            for j in range(0, i):
                s -= chunks[j]
            s %= self.k
            chunks.append(s)
        return chunks


    def restore_secret(self, chunks: list) -> int:
        return sum(chunks) % self.k


class ShamirSecretGenerator:
    def __init__(self, s: int = next_prime(999), n: int = 999, t: int = 99):
        self.s = s
        self.n = n
        self.t = t
        self.p = self._get_fitting_p()
        self.a_numbers = [randrange(999999999) for _ in range(1, self.t)]
        self.chunks = [(i, self._generate_key(i)) for i in range(1, self.n + 1)]
    
    def _get_fitting_p(self):
        p = next_prime(3000)
        while p < self.s or p < self.n:
            p = next_prime(p)
        return p

    def _generate_key(self, x: int):
        total = self.s
        for j in range(1, self.t):
            total += (self.a_numbers[j-1] * pow(x,j))
        return total % self.p

    def restore_secret(self) -> int:
        x, y = zip(*self.chunks[:self.t])
        return lagrange_interpolate(0, x, y, self.p)




trivial_gen = TrivialSecretGenerator()
trivials = trivial_gen.secret_to_chunks()
assert trivial_gen.s == trivial_gen.restore_secret(trivials), "Trivial secret not restored correctly."

shamir_gen = ShamirSecretGenerator()
assert shamir_gen.s == shamir_gen.restore_secret(), "Shamir secret not restored correctly."
