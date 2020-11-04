def gen_key(keyword: str, size: int) -> str:
    res = []
    for i in range(size):
        res.append(keyword[i % len(keyword)])
    return "".join(res)


def encrypt(data: str, key: str) -> str:
    res = []
    for raw, cipher in zip(data, key):
        vigenered = (ord(raw) + ord(cipher)) % 26
        res.append(chr(ord("A") + vigenered))
    return "".join(res)


def decrypt(data: str, key: str) -> str:
    res = []
    for raw, cipher in zip(data, key):
        vigenered = (ord(raw) - ord(cipher) % 26) % 26
        res.append(chr(ord("A") + vigenered))
    return "".join(res)


if __name__ == "__main__":
    raw = input("Enter data to encrypt: ")
    keyword = input("Enter keyword: ")
    key = gen_key(keyword, len(raw))
    encrypted = encrypt(raw, key)
    print("Genereted key: ", key)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypt(encrypted, key))
