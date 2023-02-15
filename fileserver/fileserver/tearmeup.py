#!/usr/bin/env python3
"""Make a file smaller than 1M

Chop up a base64 file into smaller than 1M files. This is needed
due to a limitation with powershell empire's limit of 1M files.
"""

import glob


def file_check() -> None:
    """Check for our base64 file and throw exception if not found"""
    seek_file = 'xmrig.b64'
    check_for_file = glob.glob(seek_file)
    if not check_for_file[0]:
        raise ValueError('File xmrig.b64 does not exist!')


def read_b64_file() -> str:
    """Read the xmrig file that is base64 encoded"""
    with open('xmrig.b64', 'r') as b64_file:
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

    file_check()
    b64_string = read_b64_file()
    chunk_files(b64_string)


if __name__ == '__main__':
    main()
