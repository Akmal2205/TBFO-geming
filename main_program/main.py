import argparse
from HtmlParser import HtmlParser
from txtParser import txtParser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process two files.')
    parser.add_argument('file1', type=str, help='First file name')
    parser.add_argument('file2', type=str, help='Second file name')

    args = parser.parse_args()

    file1 = args.file1
    file2 = args.file2

print(txtParser(file1))
print(HtmlParser(file2))




