import filetype
from PIL import Image

import os

from .img_exception import *
from utils.v_logger import ProgramStatus


IMG_WIDTH = 40
IMG_HEIGHT = 192


class ImgProcessor:
    def __init__(self, args, logger):
        self.img_path = args.input_img_path
        self.thrshld = args.thrshld
        self.is_color_inv = args.is_color_inv
        self.output_file_path = args.output_file_path
        self.converted_image_path = args.converted_image_path
        self.is_byte_array = args.is_byte_array
        self.is_verbose = args.is_verbose
        self.logger = logger
    
    def rev_endianess(self, value):
        return value[::-1]
    
    def pixels_to_byte(self, bin_pixels, is_reversed):
            if is_reversed:
                bin_pixels = self.rev_endianess(bin_pixels)

            hex_pixels = '{:02x}'.format((int(bin_pixels, 2)))

            if len(bin_pixels) == 4:
                hex_pixels = hex_pixels[::-1]

            return hex_pixels
    
    # TODO: implement data output to byte directive feature
    def data_to_byte(self, data):
        print("> Could not output image data to byte directive. Formatting data to hex...")
        return self.data_to_hex(data)
    
    def data_to_hex(self, data):
        bit_on = "1" if not self.is_color_inv else "0"
        bit_off = "0" if not self.is_color_inv else "1"

        pf0, pf1, pf2, pf3, pf4, pf5 = [], [], [], [], [], []
        NIBBLE = 4
        BYTE = 8

        data_to_str = list(map(str, data))

        for pixel in range(0, len(data_to_str), IMG_WIDTH):
            pf0.insert(0, self.pixels_to_byte("".join(data_to_str[pixel:pixel+NIBBLE]).replace("0", bit_on).replace("255", bit_off), True))
            pixel += NIBBLE
            pf1.insert(0, self.pixels_to_byte("".join(data_to_str[pixel:pixel+BYTE]).replace("0", bit_on).replace("255", bit_off), False))
            pixel += BYTE
            pf2.insert(0, self.pixels_to_byte("".join(data_to_str[pixel:pixel+BYTE]).replace("0", bit_on).replace("255", bit_off), True))
            pixel += BYTE
            pf3.insert(0, self.pixels_to_byte("".join(data_to_str[pixel:pixel+NIBBLE]).replace("0", bit_on).replace("255", bit_off), True))
            pixel += NIBBLE
            pf4.insert(0, self.pixels_to_byte("".join(data_to_str[pixel:pixel+BYTE]).replace("0", bit_on).replace("255", bit_off), False))
            pixel += BYTE
            pf5.insert(0, self.pixels_to_byte("".join(data_to_str[pixel:pixel+BYTE]).replace("0", bit_on).replace("255", bit_off), True))

        playfield = [pf0, pf1, pf2, pf3, pf4, pf5]
        playfield_data = ""

        for i, field in enumerate(playfield):
            playfield_data += f"PFBitmap{i}\n\thex 00"

            for byte in range(len(field)):
                if byte % 16 == 0:
                    playfield_data += '\n\thex '
                playfield_data += field[byte]

            playfield_data += "\n\n"

        return playfield_data

    def is_valid_img(self):
        if not os.path.exists(self.img_path):
            raise InvalidImageError(ImageErr.INVALID_IMG_PATH, self.img_path)
        elif not filetype.is_image(self.img_path):
            raise InvalidImageError(ImageErr.INVALID_IMG_FILE, self.img_path)

    def output_converted_img(self, img):
        file_name, file_extension = os.path.splitext(self.converted_image_path)

        if file_extension:
            img_path = self.converted_image_path
        else:
            img_path = os.path.join(file_name + ".png")

        img.save(img_path)
        self.logger.log(ProgramStatus.IMG_SAVED, img_path)

    def convert_img(self):
        img = Image.open(self.img_path)
        f = lambda p : 255 if p > self.thrshld else 0
        img = img.convert('L').point(f, mode='1')
        img = img.resize((IMG_WIDTH, IMG_HEIGHT))
        self.logger.log(ProgramStatus.IMG_CONVERTED)

        if self.converted_image_path:
            self.output_converted_img(img)
        
        return img

    def parse_img_pixels(self, img: Image):
        try:
            pixel_data = list(img.getdata())
            self.logger.log(ProgramStatus.PIXELS_PARSED)
            return pixel_data
        except Exception as e:
            print(f"{e}")
            raise InvalidImageError(ImageErr.INVALID_IMG, self.img_path) from e

    def create_playfield_data(self, data):
        playfield_directive = "byte" if self.is_byte_array else "hex"
        self.logger.log(ProgramStatus.CREATING_PLAYFIELD, playfield_directive)

        if self.is_byte_array:
            return self.data_to_byte(data)
        
        return self.data_to_hex(data)