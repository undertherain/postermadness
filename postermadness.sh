# poster madness script
# displays posters one by one for $duration secons
 
duration=70
path_posters="./source/"

if ! [ -x "$(command -v impressive)" ]; then
  echo 'Error: impressive is not installed.' >&2
  exit 1
fi


# for file in ./source/*
#for file in `find $path_posters -type f -name "*.pdf" | sort | awk 'NF { print "\""$0"\""}'`  

#echo $files_lines
declare -a files=(`find $path_posters -type f -name "*.pdf" | sort | awk 'NF { print "\""$0"\""}'`)
echo ${files[0]}

for file in "${files[@]}";
do
    # clear
    printf "\n\n"
    # cowsay up next: ${file:9}
    echo up next $file
    printf "\n\npress ENTER to start"
    read
    # file=$(printf '%q' "$file")
    impressive \
	-a $duration --autoquit --duration $duration --time-display \
	--fontsize 28 --font /usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf $file
done
