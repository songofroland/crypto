from itertools import islice

import numpy as np
from PIL import Image

from utils import visualize_array, random_string


def yield_pixels(img: np.ndarray):
    for row in img:
        for pixel_array in row:
            yield pixel_array


def encode_in_image(img: np.ndarray, data: bytes) -> np.ndarray:
    if len(data) * 8 > img.size:
        raise RuntimeError("Too much data to encode in this image.")

    triple_bits = np.array_split(np.unpackbits(data), len(data) * 8 / 3)
    for pixel, bits in zip(yield_pixels(img), triple_bits):
        for i in range(len(pixel)):
            pixel.put(i, (pixel[i] & ~1) | bits[i])
    return img


def bits_to_string(bits: list) -> str:
    return "".join(
        [
            chr(int("".join(map(str, bits[i : i + 8])), 2))
            for i in range(0, len(bits), 8)
        ]
    )


def decode_from_image(img: np.ndarray, size: int) -> str:
    if size > img.size:
        raise RuntimeError("Too much data to decode from this image.")

    return bits_to_string(
        [p & 1 for p in islice(yield_pixels(img), size // 3) for p in p]
    )


if __name__ == "__main__":
    with open("crypto/media/jp2.jpg", "rb") as input_image:
        source_image = Image.open(input_image)
        source_image = np.asarray(source_image).copy()
        visualize_array(source_image)

        payload = random_string(300000)
        encoded = encode_in_image(source_image, bytearray(payload, "ascii"))
        visualize_array(encoded)
        decoded = decode_from_image(encoded, len(payload) * 8)
        assert decoded == payload
