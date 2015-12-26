#!/bin/sh

# Find path of directory
SCRIPTPATH=$(readlink -f "$0")
SCRIPTDIR=$(dirname "$SCRIPTPATH")

# Run main.py every 30 minutes
echo "0,30 * * * * $SCRIPTDIR/main.py" | crontab -

echo "Crontab sucessfully added! Wallpaper will change every 30 minutes. To uninstall: \"crontab -r\""
