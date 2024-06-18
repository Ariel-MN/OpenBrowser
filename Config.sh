#!/bin/bash

# Verify if the process are already running.
proc1=$(ps aux | grep "[/]OpenBrowser/Config.py")

# Launch new process while preventing duplicates.
if [ -z $proc1 ]; then
  python3 -m idlelib.idle /home/$USER/Bin/Crypto/OpenBrowser/Config.py
fi
