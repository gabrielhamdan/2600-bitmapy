import argparse
from argparse import RawTextHelpFormatter
from dataclasses import dataclass


DEFAULT_THRSHLD_VALUE = 150


def parser_init(banner):
    parser = argparse.ArgumentParser(description=banner, formatter_class=RawTextHelpFormatter)
    parser.add_argument("-i", "--input-image", action="store", help="input image", required=True)
    parser.add_argument("-t", "--thrshld", action="store", type=int, default=DEFAULT_THRSHLD_VALUE, help="set image conversion thresholding")
    parser.add_argument("-I", "--invert-color", action="store_true", help="invert pixel color")
    parser.add_argument("-o", "--output-file", action="store", help="output file name")
    parser.add_argument("-s", "--save", action="store", help="save converted image")
    parser.add_argument("-b", "--byte-array", action="store_true", help="output byte arrays (hex by default)")
    parser.add_argument("-v", "--verbose", action="store_true", help="execute on verbose mode")
    return parser.parse_args()


@dataclass
class CommandLineArgs:
    input_img_path: str
    thrshld: int
    is_color_inv: bool
    output_file_path: str
    converted_image_path: str
    is_byte_array: bool
    is_verbose: bool


def parse_cli(banner):
    args = parser_init(banner)

    return CommandLineArgs(
        input_img_path = args.input_image,
        thrshld = args.thrshld,
        is_color_inv = args.invert_color,
        output_file_path = args.output_file,
        converted_image_path = args.save,
        is_byte_array = args.byte_array,
        is_verbose = args.verbose
    )