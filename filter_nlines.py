#!/usr/bin/python3

from argparse import ArgumentParser
import itertools
import os
import sys

def files(filename):
    if not os.path.isfile(filename):
        raise ValueError("File {} not found".format(filename))
    return filename

def parse_arguments():
    parser = ArgumentParser(description="Extract all n lines from files or standard input.")

    parser.add_argument("n", type=int, help="Which lines to extract")
    parser.add_argument("-fs", "--from-start", action="store_true", help="Start counting from the second line (force output of the first line). This comes after -s during processing.")
    parser.add_argument("-s", "--skip", metavar="N", type=int, help="Ignore the first N lines of input (for each file if files are specified). This takes precedence over -fs.")
    parser.add_argument("files", type=files, help="List of files to process", nargs="*")

    return parser.parse_args()

def process_input(input_iter, arguments):
    if arguments.skip:
        lines = itertools.islice(input_iter, arguments.skip, None)
    else:
        lines = input_iter

    if arguments.from_start:
        lines = itertools.islice(lines, 0, None, arguments.n)
    else:
        lines = itertools.islice(lines, arguments.n - 1, None, arguments.n)

    for line in lines:
        if line[-1] == "\n":
            print (line[:-1])
        else:
            print (line)

def process(parse_result):
    if not len(parse_result.files):
        process_input(sys.stdin.readlines(), parse_result)
    else:
        for filename in parse_result.files:
            with open(filename) as f:
                process_input(f.readlines(), parse_result)

if __name__ == "__main__":
    parse_result = parse_arguments()
    process(parse_result)
