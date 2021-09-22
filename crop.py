#!/usr/bin/env python

import argparse
import imageio


parser = argparse.ArgumentParser()
parser.add_argument('input', default='image.png',
                    help="Path to the input image to be cropped")
parser.add_argument('--output',
                    help="Path to the output image to be saved")


parser.add_argument('--he', default=['0', '10'], nargs=2, type=int,
                    help="Height coordinates")
parser.add_argument('--wi', default=['0', '20'], nargs=2, type=int,
                    help="Width coordinates")

args = parser.parse_args()

image = imageio.imread(args.input)

if args.output is None:
    args.output = args.input[: args.input.rfind('.')] + '_crop' + args.input[args.input.rfind('.') :]

if len(image.shape) == 3:
    image_crop = image[args.he[0]:args.he[1], args.wi[0]:args.wi[1], :]
else:
    image_crop = image[args.he[0]:args.he[1], args.wi[0]:args.wi[1]]

imageio.imsave(args.output, image_crop)