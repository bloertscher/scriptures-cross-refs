# D&C
wget -w 0.1 --random-wait -r -nc --no-parent -l inf -i dc-list -o dc-log --reject-regex "[0-9]+\."
# Rest of scriptures
wget -w 0.5 --random-wait -r -nc --no-parent -l inf -i scriptures-list -o scriptures-log
# Rename without '?lang=eng'
find . -iname '*\?*' | xargs -I % sh -c 'newname=$(echo % | sed "s/\(^.*\)\(\?.*\)/\1/"); mv % $newname'