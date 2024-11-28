
from spleeter.separator import Separator

class SpleeterWrapper:
    def __init__(self):
        self.separator = Separator('spleeter:2stems')

    def separate(self, input_file, output_dir):
        self.separator.separate_to_file(input_file, output_dir)
