from enum import Enum


class ProgramStatus(Enum):
    INIT = "{}\n\n> 2600 Bitmapy initialized."
    IMG_CONVERTED = "Image converted with success."
    IMG_SAVED = "Converted image saved as {}."
    PIXELS_PARSED = "Pixels parsed."
    CREATING_PLAYFIELD = "Creating playfield as {}."
    FILE_CREATED = "Output file created as {}."
    EXIT = "Success! Time of execution: {} milliseconds.\n> Happy coding!"


class VLogger:
    def __init__(self, verbose=True):
        self.verbose = verbose

    def log(self, message, *args):
        if self.verbose:
            template = self.format_log(message.value, args)
            if message == ProgramStatus.INIT:
                print(template)
            else:
                print("> " + template)

    def format_log(self, log, args):
        formatted_args = [str(arg) for arg in args]
        return log.format(*formatted_args)