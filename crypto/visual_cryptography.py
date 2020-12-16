import random
from typing import List
from datetime import datetime
from typing import List

from PIL import Image

BLACK = 0
WHITE = 255


def visualize_matrix(matrix: List[list]) -> None:
    image = Image.new("1", (len(matrix[0]), len(matrix)))
    for i in range(image.height):
        for j in range(image.width):
            image.putpixel((j, i), matrix[i][j])
    image.show()


def merge_images(img_matrix_1: List[list], img_matrix_2: List[list]) -> Image:
    image = Image.new("1", (len(img_matrix_1[0]), len(img_matrix_1)))
    for i in range(image.height):
        for j in range(image.width):
            image.putpixel((j, i), min(img_matrix_2[i][j], img_matrix_1[i][j]))
    return image


if __name__ == "__main__":
    with open("crypto/media/visual_cryptography_source.png", "rb") as input_image:
        source_image = Image.open(input_image)

        # Should be used numpy here
        first_img: List[list] = [[] for _ in range(source_image.height)]
        second_img: List[list] = [[] for _ in range(source_image.height)]

        blacks = [[(BLACK, WHITE), (WHITE, BLACK)], [(WHITE, BLACK), (BLACK, WHITE)]]
        whites = [[(BLACK, WHITE), (BLACK, WHITE)], [(WHITE, BLACK), (WHITE, BLACK)]]

        for i in range(source_image.height):
            for j in range(source_image.width):
                if source_image.getpixel((j, i)) == WHITE:
                    w_matrix = random.choice(whites)
                    first_img[i].extend(w_matrix[0])
                    second_img[i].extend(w_matrix[1])
                else:
                    b_matrix = random.choice(blacks)
                    first_img[i].extend(b_matrix[0])
                    second_img[i].extend(b_matrix[1])

        visualize_matrix(first_img)
        visualize_matrix(second_img)
        merge_images(first_img, second_img).show()
