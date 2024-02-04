"""
This module only convert text, pdf, docx, doc, and other files into string
"""

# indentifying of the file:

# def get_file_type(file_path):
#     _, file_extension = os.path.splitext(file_path)
#     return file_extension


class Stringify:
    """
    This module has functions responsible for converting files into 'string'
    """

    def __init__(self, file):
        self.__file = file

    def text_converter(self):
        with open(self.__file, "r", encoding="UTF-8") as file:
            h_file = file.read()
            return h_file
