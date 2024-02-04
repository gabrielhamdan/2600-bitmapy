from enum import Enum


class ImageErr(Enum):
    INVALID_IMG = "invalid image"
    INVALID_IMG_PATH = "invalid image path"
    INVALID_IMG_FILE = "invalid image file"


class InvalidImageError(Exception):
    def __init__(self, err_code=ImageErr.INVALID_IMG, path=None):
        self.err_code = err_code
        self.path = path
        self.message = self.err_code.value
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidImageError: {self.message} '{self.path}'"
