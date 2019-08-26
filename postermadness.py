from pathlib import Path
import os

path_source = "source"
duration=70

for filename in sorted(Path(path_source).glob('**/*.pdf')):
    print("up next:", filename.name)

    os.system(f"impressive -a {duration} --autoquit --duration {duration} --time-display --fontsize 28 --font /usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf {filename}")
