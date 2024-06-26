#!/usr/bin/env python3
"""Make a file smaller than 1M

Chop up a base64 file into smaller than 1M files. This is needed
due to a limitation with powershell empire's limit of 1M files.
"""

import argparse
import glob

# SEEK_FILE = 'xmrig.b64'


def parse_arguments() -> tuple:
    """Obtain user input and parse"""
    user_license = 'Copyright (C) 2017  Mitch O\'Donnell\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.'
    url_repo = 'https://github.com/BuildAndDestroy/powershell-empire-custom'
    epilog = '{}\n\n{}'.format(user_license, url_repo)

    parser = argparse.ArgumentParser(
        description=__doc__, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        'file_name', help='File you wish to shred into 1M files.\n    [*] Example: xmrig.b64')
    args = parser.parse_args()

    return args


def file_check(file_name) -> None:
    """Check for our base64 file and throw exception if not found"""
    check_for_file = glob.glob(file_name)
    if not check_for_file:
        raise ValueError(f'File {file_name} does not exist!')


def read_b64_file(file_name) -> str:
    """Read the file that is base64 encoded"""
    with open(file_name, 'r') as b64_file:
        b64_string = b64_file.read()
    return b64_string


def chunk_files(b64_string) -> None:
    """Accepts base64 string and prints into <1M files"""
    size = 999999
    counter = 1
    for i in range(0, len(b64_string), size):
        with open(f'file_{counter}', 'w') as b64_file:
            b64_file.write(b64_string[i:i+size])
        counter += 1
    return


def main() -> None:
    """Execute the program"""

    args = parse_arguments()
    file_check(args.file_name)
    b64_string = read_b64_file(args.file_name)
    chunk_files(b64_string)


if __name__ == '__main__':
    main()
