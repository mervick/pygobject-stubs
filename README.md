# pygobject-stubs
Stubs for PyGObject auto generated with pycharm-community/plugins/python-ce/helpers/generator3

![demo1](/img/Peek-2020-06-06-00-33.gif?raw=true)

![demo2](/img/Peek-2020-06-06-00-34.gif?raw=true)

## how to use this

```bash
git clone https://github.com/ttys3/pygobject-stubs.git /tmp/
mv /tmp/pygobject-stubs/gi-stubs ~/.local/lib/python3.8/site-packages/
```

pycharm should use the stubs now.

## generate all stubs

```bash
git clone --depth 1 https://github.com/JetBrains/intellij-community.git /tmp/idea

mkdir /tmp/out
libpath=/usr/lib64/girepository-1.0
[[ ! -d $libpath ]] && libpath=/usr/lib/girepository-1.0

for filelib in $(ls -1 $path); do
    typelib=${filelib%-*}
    echo "generating $typelib"
    python3 /tmp/idea/python/helpers/generator3/__main__.py -d /tmp/out -p "gi.repository.$typelib" "$libpath/$filelib"
done

#make pyCharm can use it:
mv /tmp/out/gi ~/.local/lib/python3.8/site-packages/gi-stubs
# or you can put the gi-stubs dir to anywhere but just remember to add to your project
# see https://www.jetbrains.com/help/pycharm/stubs.html#reuse-stubs
```
