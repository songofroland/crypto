import hashlib

hash_funcs = {
    "1": hashlib.md5,
    "2": hashlib.sha1,
    "3": hashlib.sha256,
    "4": hashlib.sha384,
    "5": hashlib.sha512,
    "6": hashlib.sha3_224,
    "7": hashlib.sha3_256,
    "8": hashlib.sha3_384,
    "9": hashlib.sha3_512,
}

while True:
    method = 0
    while method not in hash_funcs:
        method = input(
            "Please select hash method:"
            "\n1 - MD5\n2 - SHA-1\n3 - SHA2(256)\n4 - SHA2(384)\n5 - SHA2(512)\n"
            "6 - SHA-3(256)\n7 - SHA-3(384)\n8 - SHA-3(512)\n"
        )
    data = input("Plese enter word to hash: ")
    print(f"\nCalculated hash: {hash_funcs[method](data.encode()).hexdigest()}\n")
