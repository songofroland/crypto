from decimal import Decimal
from utils import get_modular_inverse, get_smallest_co_prime, next_prime


class RSA:
    def __init__(self):
        self._p = next_prime(3000)
        self._q = next_prime(self._p)
        self.n = self._p * self._q
        self.phi = (self._p - 1) * (self._q - 1)
        self.e = get_smallest_co_prime(self.phi)
        self.d = get_modular_inverse(self.e, self.phi)

    def cipher(self, number: int) -> int:
        return pow(number, self.e, self.n)

    def decipher(self, number: int) -> int:
        return pow(number, self.d, self.n)


generator = RSA()

message = "Jacek Sasin zmarnowal 70 milionow zlotych polskich."
numbered_message = [ord(s) for s in message]
cipher = [generator.cipher(h) for h in numbered_message]
deciphered = [generator.decipher(c) for c in cipher]
assert message == "".join([chr(d) for d in deciphered])