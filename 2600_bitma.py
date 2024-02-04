import os
import sys
import time

from utils import cli_parser
from img_processing.img_processor import ImgProcessor
from img_processing.img_exception import InvalidImageError
from utils.v_logger import *


CLI = sys.argv[0]
BANNER_PATH = "data/banner"
START_TIME = time.time()

with open(BANNER_PATH) as f:
    BANNER = f.read()

args = cli_parser.parse_cli(BANNER)
logger = VLogger(args.is_verbose)
img_processor = ImgProcessor(args, logger)
logger.log(ProgramStatus.INIT, BANNER)

try:
    img_processor.is_valid_img()
except InvalidImageError as e:
    print(f"{CLI}: {e}")
    sys.exit(1)

def output_file():
    output_file_name = args.output_file_path

    if not output_file_name:
        output_file_name, _ = os.path.splitext(args.input_img_path)
    
    with open(output_file_name, 'w') as file:
        file.write(playfield_data)

converted_img = img_processor.convert_img()
img_pixel_data = img_processor.parse_img_pixels(converted_img)
playfield_data = img_processor.create_playfield_data(img_pixel_data)

output_file()

ELAPSED_TIME = (time.time() - START_TIME) * 1000
ELAPSED_TIME_MILLI = f"{ELAPSED_TIME:.2f}"
logger.log(ProgramStatus.EXIT, ELAPSED_TIME_MILLI)
sys.exit(0)