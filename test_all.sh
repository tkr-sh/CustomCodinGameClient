#!/bin/zsh

success=0
tot=0
fail=()


for file in $(ls "test"); do
    # Get the name
    name=$(echo "$file" | cut -d '.' -f 1)
    echo "Testing '$name':"

    # Capture the stdout
    output=$(./test.sh $name >&1)

    # Echo it
    echo $output;

    # Check if correct
    if [[ "$output" =~ "Success!" ]]; then
       success=$[ success + 1 ]
    else 
        fail+=($name)
    fi


    # Wait
    sleep 0.1

    # Add 1 to the tot
    tot=$[ tot + 1 ]
done




echo "\nResult: \033[032m$success\033[0m/$tot\n"



if [[ ${#fail[@]} -eq 0 ]]; then
        echo "\033[042m========= SUCCESS =========\033[0m"

else
    echo "\033[041m========== FAIL ==========\033[0m"

    # Echo all fails
    for e in "${fail[@]}"; do
        echo "\033[031mError\033[0m in: $e.\033[033mpy\033[0m"
    done
fi 