import time
import pprint

from Crypto.Cipher import AES

block_modes = ("MODE_ECB", "MODE_CBC", "MODE_OFB", "MODE_CFB", "MODE_CTR")
sample_files = ("large.dat", "medium.dat", "small.dat")

r = {s.replace(".dat", ""): None for s in sample_files}
results = {m: {"encrypt": r.copy(), "decrypt": r.copy()} for m in block_modes}


def benchmark(mode: str) -> dict:
    for f_name in sample_files:
        with open(f_name, "rb") as f:
            b = f.read()
            encrypted_file = "encrypted_" + f_name
            with open(encrypted_file, "wb") as wf:
                encoder = AES.new(b"Sixteen byte key", getattr(AES, mode))
                start = time.time()
                s = encoder.encrypt(b)
                res = time.time() - start
                wf.write(s)
                results[mode]["encrypt"][f_name.replace(".dat", "")] = res
            with open(encrypted_file, "rb") as rf:
                decoder = AES.new(b"Sixteen byte key", getattr(AES, mode))
                start = time.time()
                decoder.decrypt(b)
                res = time.time() - start
                results[mode]["decrypt"][f_name.replace(".dat", "")] = res


for mode in block_modes:
    benchmark(mode)

pprint.PrettyPrinter(indent=4).pprint(results)