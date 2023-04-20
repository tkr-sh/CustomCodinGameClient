#!/bin/zsh
# ========

# Get the lang and extract the test program and the extension
lang=$(echo "$1" | tr 'A-Z' 'a-z')
nb_inputs=$2
tmpDir="$3"

# Go to the test directory
cd tmp/$tmpDir
echo $tmpDir
pwd
# Copy the script to launch programs
cp ../../Docker/$lang/launch.sh .



# Run the docker
timeout --preserve-status -s 9 60 \
        docker run                                                \
        --mount type=bind,source=`pwd`,target=/tmp/in,ro          \
        --mount type=bind,source=`pwd`,target=/tmp/out            \
        --memory 512mb                                            \
        --network none                                            \
        --name codingame-$lang-$$ --rm                             \
        "codingame-$lang"":latest" /bin/sh /tmp/in/launch.sh  $(( $nb_inputs - 1 ))
