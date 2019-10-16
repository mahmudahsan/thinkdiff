#!/bin/sh

kill $(ps aux | grep "Safari")

python3 /Users/mahmud/Desktop/demo/web/browser-script.py /Users/mahmud/Desktop/demo/web/websites.txt safari
exit 0