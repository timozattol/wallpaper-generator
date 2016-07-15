#!/bin/sh

# Find path of directory
SCRIPTPATH=$(readlink -f "$0")
SCRIPTDIR=$(dirname "$SCRIPTPATH")

# Find resolution dynamically
resolution=$(xdpyinfo | awk '/dimensions/{print $2}')

echo "Using resolution: $resolution"

# Run main.py every 30 minutes
echo "0,30 * * * * $SCRIPTDIR/main.py" "$resolution" | crontab -

echo "Crontab sucessfully added! Wallpaper will change every 30 minutes. To uninstall: \"crontab -r\""
