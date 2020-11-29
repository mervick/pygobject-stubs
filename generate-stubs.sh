#!/usr/bin/env bash

git clone --depth 1 https://github.com/JetBrains/intellij-community.git /tmp/idea

mkdir /tmp/out
libpath=/usr/lib64/girepository-1.0
[[ ! -d $libpath ]] && libpath=/usr/lib/girepository-1.0

for filelib in $(ls -1 $path); do
    typelib=${filelib%-*}
    echo "generating $typelib"
    python3 /tmp/idea/python/helpers/generator3/__main__.py -d /tmp/out -p "gi.repository.$typelib" "$libpath/$filelib"
done

