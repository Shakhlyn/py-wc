import sys
import argparse

from counter import WC

def wc():
    
    # If false, coming from piping, not terminal
    if not sys.stdin.isatty:
        text = sys.stdin.read()
        
        wc = WC(text)
        
        size = wc.byte_counter()
        chars =wc.char_counter()
        word  = wc.word_counter()
        line = wc.line_counter()
        
        print(size, chars, word, line)
        return size, chars, word, line
    
    
    # catch from terminal with 'argparse'
    else:
        # creating a parser
        parser = argparse.ArgumentParser(description="Catch arguments and process")
        
        # adding arguments
        parser.add_argument(
            "file", help="Only text file should be passed"
        )
        
        parser.add_argument('-c', '--bytesize', type=str, action="store_true", help='Find the total size of the file in byte')
        parser.add_argument('-w', '--word', type=str, action="store_true", help='Find the total words of the file')
        
        
        # parsing arguments
        args = parser.parse_args()
        
        # accessing argument values