# poster madness script
# displays posters one by one for $duration secons
 
duration=70
for file in ./source/*
do
    clear
    printf "\n\n"
    cowsay up next: ${file:9}
    printf "\n\npress ENTER to start"
    read
    file=$(printf '%q' "$file")
    impressive \
	-a $duration --autoquit --duration $duration --time-display \
	--fontsize 28 --font /usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf $file
done