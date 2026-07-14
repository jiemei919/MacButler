#!/bin/bash

CACHE="$HOME/Library/Containers/com.bytedance.macos.feishu/Data/Library/Caches"
DATA="$HOME/Library/Containers/com.bytedance.macos.feishu/Data/Library/Application Support"

CACHE_SIZE=$(du -sh "$CACHE" 2>/dev/null | awk '{print $1}')
DATA_SIZE=$(du -sh "$DATA" 2>/dev/null | awk '{print $1}')

echo "CACHE_SIZE=$CACHE_SIZE"
echo "DATA_SIZE=$DATA_SIZE"
echo "RISK=MEDIUM"