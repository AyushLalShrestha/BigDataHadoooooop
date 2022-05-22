
from collections import defaultdict
import os
width = 25
height = 6
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def read_from_file(file_path):
    with open(file_path, "r") as fh:
        inputs = fh.read()
        for i in inputs:
            yield i


def find_applied_color(seq, index):
    for i, image in seq.items():
        if image[index] != 2:
            return image[index]
    return 2


if __name__ == "__main__":
    inputseq = read_from_file(os.path.join(CURRENT_PATH, "input.txt"))
    # inputseq = [0,2,2,2,1,1,2,2,2,2,1,2,0,0,0,0]
    image = defaultdict(list)
    quota = width * height
    image_number = 1
    for i in inputseq:
        image[image_number].append(int(i))
        quota -= 1
        if quota == 0:
            quota = width * height
            image_number += 1

    # -- part 1 --
    # min_no_zeros = float("inf")
    # min_zeros_image = None
    # for i, pixels in image.items():
    #     number_of_zeros = pixels.count(0)
    #     if number_of_zeros < min_no_zeros:
    #         min_zeros_image = pixels
    #         min_no_zeros = number_of_zeros
    # print(min_zeros_image.count(1) * min_zeros_image.count(2))
    # - - - - - end of part 1 - - - - - - - 

    # -- part 2 --
    result_image = list()
    for i in range(quota):
        color = find_applied_color(image, i)
        result_image.append(color)

    width_count = 1
    line = ""
    for i in result_image:
        if width_count > width:
            width_count = 1
            print(line)
            line = ""
        if i == 0:
            line += "."
        elif i == 1:
            line += "#"
        width_count += 1
    print(line)