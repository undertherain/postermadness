from pathlib import Path
import os
import subprocess

path_source = "source"
duration = 70


def clear():
    # check and make call for specific operating system 
    subprocess.run(['clear'] if os.name =='posix' else 'cls')


def check_env():
    try:
        subprocess.run(["impressive", "--version"])
    except FileNotFoundError:
        print("impressive is not installed")
        exit(-1)

check_env()
for filename in sorted(Path(path_source).glob('**/*.pdf')):
    clear()
    print("up next:", filename.name)
    input("Press Enter to start")
    command = f"impressive -a {duration} --autoquit --duration {duration}"
    command += f" --time-display --fontsize 28"
    command += f" --font /usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf \"{filename}\""
    os.system(command)
