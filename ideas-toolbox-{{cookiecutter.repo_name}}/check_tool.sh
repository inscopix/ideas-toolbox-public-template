# checks if tool is valid
# before we start the docker container,
# useful to catch user input errors

FILE=inputs/$1.json
if [ -f "$FILE" ]; then
    printf "$FILE exists."
else 
    printf "\n\n================================================="
    printf "\n[TOOL KEY ERROR] $FILE does not exist."   
    printf "\n\n Possible tools to run are:\n\n"     
    ls inputs/*.json
    printf "\n=================================================\n\n"
    exit 1
fi

FILE=commands/$1.sh
if [ -f "$FILE" ]; then
    printf "$FILE exists."
else 
    printf "\n\n================================================="
    printf "\n[TOOL KEY ERROR] $FILE does not exist."
    printf "\n\n Possible tools to run are:\n\n"     
    ls commands/*.sh
    printf "\n=================================================\n\n"
    exit 1
fi

