#!/bin/bash

# Verify if the process are already running.
proc1=$(ps aux | grep "[/]OpenBrowser/Main.pyw")

# Launch new process while preventing duplicates.
if [ -z $proc1 ]; then
  source /home/$USER/Bin/Crypto/env/bin/activate
  python /home/$USER/Bin/Crypto/OpenBrowser/Main.pyw
fi
