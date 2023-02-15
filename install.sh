#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Run as root!"
  exit
fi

echo "Copying 'src/config.py' to '/usr/bin/cp-cfg'"
install -Dm755 src/config.py /usr/bin/cp-cfg
echo "Copying 'src/presence.py' to '/usr/bin/cp-run'"
install -Dm75 src/presence.py /usr/bin/cp-run
echo "Copying 'src/config.ui' to '~/.local/share/custom-presence/config.ui'"
mkdir -p ~/.local/share/custom-presence
cp src/config.ui ~/.local/share/custom-presence/.
echo "Done!"
