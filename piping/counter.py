# def get_file_type(file_path):
#     _, file_extension = os.path.splitext(file_path)
#     return file_extension

"""
A Word counter tool that counts byte size, chars, words, lines from text, pdf files
"""

import os


class WC:
    def __init__(self, input_file):
        self.__input_file = input_file
        self.__h_file = self.__read_file()

    def __read_file(self):
        with open(self.__input_file, "r", encoding="utf-8") as file:
            return file.read()

    def byte_counter(self):
        """
        Counts the total byte of the input file in integer and return
        """
        byte_size = os.path.getsize(self.__input_file)
        return byte_size

    def char_counter(self):
        """
        Counts the total characters of the file in integer and return
        """

        total_chars = len(self.__h_file)
        return total_chars

    def word_counter(self):
        """
        Counts the total words of the file in integer and return
        """

        word_list = self.__h_file.split()  # split make list of words
        total_words = len(word_list)
        return total_words

    def line_counter(self):
        """
        Counts the total lines the file has and return in integer
        """

        new_file = self.__h_file.split("\n")
        line = len(new_file) - 1
        return line


if __name__ == "__main__":
    # FILE = "test.txt"
    FILE = "text.txt"
    wc = WC(FILE)

    CHAR = wc.char_counter()
    WORD = wc.word_counter()
    LINE = wc.line_counter()
    
    print(CHAR, WORD, LINE)
