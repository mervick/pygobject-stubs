#!/usr/bin/env bash

local=~/.local/lib/python3.6/site-packages/gi-stubs/gi/repository
for file in $(ls -1 --color=never); do
    if [[ ! -e $local/$file ]]; then
        rsync -a ./$file $local
    fi
done
