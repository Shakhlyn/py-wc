# import os
import sys
import argparse

from piping.string_generator import Stringify
from piping.counter import WC

# # indentifying of the file:

# # def get_file_type(file_path):
# #     _, file_extension = os.path.splitext(file_path)
# #     return file_extension


def parse_arguments():
    parser = argparse.ArgumentParser(description="Catch arguments and process")

    # Arguments for file processing
    parser.add_argument("file", nargs="?", help="Text file to process")

    # Optional arguments
    parser.add_argument(
        "-c",
        "--bytesize",
        action="store_true",
        help="Find the total size of the file in bytes",
    )
    parser.add_argument(
        "-m",
        "--char",
        action="store_true",
        help="Find the total characters of the file",
    )
    parser.add_argument(
        "-w",
        "--word",
        action="store_true",
        help="Find the total words of the file",
    )
    parser.add_argument(
        "-l",
        "--line",
        action="store_true",
        help="Find the total lines of the file",
    )

    return parser.parse_args()


def process_file(file_content):
    wc = WC(file_content)
    return {
        "char": wc.char_counter(),
        "word": wc.word_counter(),
        "line": wc.line_counter(),
        "byte_size": wc.byte_counter(),
    }


def ccwc():
    args = parse_arguments()

    if sys.stdin.isatty():  # From terminal
        if not args.file:
            print("Error: Please provide a file to process.")
            sys.exit(1)

        file_obj = Stringify(args.file)
        file_content = file_obj.text_converter()
    else:  # Piped input
        file_content = sys.stdin.read()

    results = process_file(file_content)

    if args.line or args.word or args.bytesize or args.char:
        output = ""
        if args.line:
            output += f"line: {results['line']}\t"
        if args.word:
            output += f"word: {results['word']}\t"
        if args.bytesize:
            output += f"byte_size: {results['byte_size']}\t"
        if args.char:
            output += f"char: {results['char']}\t"
        if args.file:
            output += args.file
        print(output)

    else:
        output = ""
        output += f"{results['line']}\t{results['word']}\t{results['byte_size']}\t{results['char']}\t"
        if args.file:
            output += args.file
        print(output)


if __name__ == "__main__":
    ccwc()
