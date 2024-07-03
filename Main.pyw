#!/usr/bin/env python3

### SCRIPT THAT OPENS CHROMIUM WINDOWS WITH DIFFERENT PROFILES ###

## Dependencies ##
    # sudo apt install python3-screeninfo (optional)
    # sudo apt-get install xdotool

import os
import time
from datetime import datetime
import subprocess
import webbrowser
from Config import *

__version__ = 'v1.0.1'

# Get the path of this script file
AppPath=os.path.dirname(__file__)

# Default screen size
ScreenWidth = 1920
ScreenHeight = 1080

def WriteLog(Level, Message):
    # Write messages to log file
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(f"{AppPath}/autostart.log", "a+") as f:
        f.write(f"{now} - [{Level}] {Message}\n")

def DesktopChange(delay):
    # Switch to next virtual desktop
    print(f"Info: Waiting {delay} seconds before switching desktop...")
    time.sleep(delay)
    SwitchError = subprocess.call("xdotool key ctrl+alt+Right", shell=True)
    if not SwitchError:
        print("Info: Desktop switched")
    else:
        print("Warning: Could't switch desktop, run 'sudo apt-get install xdotool'")

# Get screen sizes
try:
    from screeninfo import get_monitors
    ScreenWidth = get_monitors()[0].width
    ScreenHeight = get_monitors()[0].height
except Exception as E:
    WriteLog('Warning', E)

# Open browser profiles
try:
    PosWidth = Position[0]
    PosHeight = Position[1]

    #DesktopChange(10)
    for i, element in enumerate(ProfileList):
        Profile = element[0]
        Url = element[1]
        UrlIndex = UrlList.index(Url)
        
        print(f"Debug: Ind{i} - {Profile}")
        # Calculate position of new windows skipping fist window
        if i > 0:
            # Calculate the needed space in screen
            AddCol = PosWidth+Size[0]*2+MarginLeft < ScreenWidth
            AddRow = PosHeight+Size[1]*2+MarginTop < ScreenHeight
            # Calculate if window can be in a new column
            if AddCol:
                PosWidth+=Size[0]+MarginLeft
            # Calculate if window can be in a new row
            elif AddRow:
                PosHeight+=Size[1]+MarginTop
                # Set width to start value for initialize the next row
                PosWidth=Position[0]
            # Change to the next virtual desktop and reset positions
            elif (not AddCol) and (not AddRow):
                DesktopChange(40)
                PosWidth=Position[0]
                PosHeight=Position[1]
            print(f"Debug: AddCol={AddCol}; AddRow={AddRow}")
        print(f"Debug: PosWidth={PosWidth}; PosHeight={PosHeight}")

        # Config Browser Options:
        # https://peter.sh/experiments/chromium-command-line-switches/#window-name
        browser = ' '.join([
        "chromium",
        "--allow-silent-push",
        "--enable-webgl",
        "--ignore-gpu-blacklist",
        "--disable-gpu",
        f'--window-name="{Profile} - Url {UrlIndex}"',
        f"--profile-directory={Profile}",
        f"--user-data-dir={AppPath}/WebProfiles/{Profile}/UserData{UrlIndex}",
        f"--window-size={Size[0]},{Size[1]}",
        f"--window-position={PosWidth},{PosHeight}",
        "--app=%s &",
        ])
        # Slow down the process
        time.sleep(2)
        # Open Browser profile window
        webbrowser.get(browser).open_new(Url)

except Exception as E:
    WriteLog('Error', E)
