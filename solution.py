import os
import sys
import argparse
from math import sqrt
from PIL import Image


def create_arg_parser():
    parser = argparse.ArgumentParser(description="The test task on images similarity")
    parser.add_argument('--path', help='folder with images', required=True)
    return parser


def compare(im1, im2):
    size_const = 32
    imc1 = im1.resize((size_const, size_const), Image.ANTIALIAS)
    imc2 = im2.resize((size_const, size_const), Image.ANTIALIAS)

    pixels1 = imc1.load()
    pixels2 = imc2.load()

    res = 0
    for i in range(size_const):
        for j in range(size_const):
            res = res + (pixels1[i, j][0] - pixels2[i, j][0]) ** 2 + (pixels1[i, j][1] - pixels2[i, j][1]) ** 2 + (
                    pixels1[i, j][2] - pixels2[i, j][2]) ** 2
    return sqrt(res) / (size_const ** 2)


def printer(duplicate, modification, similar):
    print("Duplicate:")
    for i in duplicate:
        print(i)
    print("Modification:")
    for i in modification:
        print(i)
    print("Supposed to be similar:")
    for i in similar:
        print(i)


if __name__ == '__main__':
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    directory = parsed_args.path
    files = os.listdir(directory)
    duplicate = list()
    modification = list()
    similar = list()
    for i in range(len(files)):
        im1 = Image.open(os.path.join(directory, files[i]))
        for j in range(i + 1, (len(files))):
            im2 = Image.open(os.path.join(directory, files[j]))
            diff = compare(im1, im2)
            if diff == 0.0:
                duplicate.append((files[i], files[j]))
            elif diff < 1:
                modification.append((files[i], files[j]))
            elif 1 <= diff < 2.5:
                similar.append((files[i], files[j]))

    printer(duplicate, modification, similar)
