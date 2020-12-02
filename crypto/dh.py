from random import randrange

from utils import next_prime, get_primitive_root


class DHClient:
    n = next_prime(10 ** 6)
    g = get_primitive_root(n)

    def __init__(self):
        self.private_key = randrange(10 ** 6)
        self.public_key = (self.g ** self.private_key) % self.n

    def get_session_key(self, public_key: int) -> int:
        return (public_key ** self.private_key) % self.n


A = DHClient()
B = DHClient()

print("A's public key: ", A.public_key)
print("A's private key: ", A.private_key)
print("A's session key: ", A.get_session_key(B.public_key))
print("B's public key: ", B.public_key)
print("B's private key: ", B.private_key)
print("B's session key: ", B.get_session_key(A.public_key))
