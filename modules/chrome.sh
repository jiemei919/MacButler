#!/bin/bash

CHROME="$HOME/Library/Application Support/Google/Chrome/Default"

if [ ! -d "$CHROME" ]; then
    echo "CACHE_SIZE=0 MB"
    echo "RISK=LOW"
    exit
fi

SIZE=$(du -sh "$CHROME/Service Worker" 2>/dev/null | awk '{print $1}')

NUM=$(echo "$SIZE" | sed 's/G//')

if (( $(echo "$NUM > 5" | bc -l) )); then
    RISK="HIGH"
else
    RISK="LOW"
fi

echo "CACHE_SIZE=$SIZE"
echo "RISK=$RISK"