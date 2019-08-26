"""
Poster Madness is a script to support lightning talks-style presentation
it displays pdf files from source_dir directory one after another automatically
with auto-advance and nice progress bar

imressive is used as a pdf viewer
"""

from pathlib import Path
import os
import argparse
import subprocess


def clear():
    subprocess.run(['clear'] if os.name == 'posix' else 'cls')


def check_env():
    try:
        subprocess.run(["impressive", "--version"])
    except FileNotFoundError:
        print("impressive is not installed")
        exit(-1)


def main():
    check_env()

    parser = argparse.ArgumentParser(description='Start poster madness!')
    parser.add_argument('source_dir', type=str, help='an integer for the accumulator')
    parser.add_argument('--duration', type=int, default=60, help='duration of one presentation')

    args = parser.parse_args()

    for filename in sorted(Path(args.source_dir).glob('**/*.pdf')):
        clear()
        print("\n\nup next:", filename.name)
        input("\n\nPress Enter to start")
        command = ["impressive", "-a", f"{args.duration}", "--autoquit", "--duration", f"{args.duration}"]
        command += ["--time-display", "--fontsize", "28"]
        command += ["--font", "/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf"]
        command += [f"{filename}"]
        subprocess.run(command)


if __name__ == "__main__":
    main()
