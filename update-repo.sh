#!/usr/bin/env bash

tmp=/tmp/out/gi/repository
for file in $(ls -1 --color=never $tmp); do
    if [[ ! -e ./$file ]]; then
        rsync -a $tmp/$file ./
    fi
done

