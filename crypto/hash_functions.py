import hashlib
import random
import string
import time
from pprint import pprint


hash_funcs = {
    "MD5": hashlib.md5,
    "SHA-1": hashlib.sha1,
    "SHA2(256)": hashlib.sha256,
    "SHA2(384)": hashlib.sha384,
    "SHA2(512)": hashlib.sha512,
    "SHA-3(224)": hashlib.sha3_224,
    "SHA-3(256)": hashlib.sha3_256,
    "SHA-3(384)": hashlib.sha3_384,
    "SHA-3(512)": hashlib.sha3_512,
}


def get_hash_and_time(method: str, data: bytes) -> tuple:
    start = time.time()
    result = hash_funcs[method](data).hexdigest()
    return result, time.time() - start


FREE_INPUT = 1
MODE = FREE_INPUT

run = True
while run:
    results = {}
    if MODE == FREE_INPUT:
        data = input("Enter the text to hash: ")
        for name, func in hash_funcs.items():
            results[name] = {}
            result, seconds = get_hash_and_time(name, data.encode())
            results[name]["hash"] = result
            results[name]["time"] = f"{seconds} seconds."
    else:
        for name, func in hash_funcs.items():
            results[name] = {}
            for size in ("small", "medium", "large"):
                with open(f"{size}.txt", "rb") as f:
                    results[name][size] = get_hash_and_time(name, f.read())[1]
        run = False

    pprint(results)
