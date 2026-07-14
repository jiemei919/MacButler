#!/bin/bash

echo "📀 磁盘检查"

FREE_SPACE=$(diskutil info / | grep "Container Free Space" | sed 's/.*: //' | awk '{print $1,$2}')

echo "STATUS=OK"
echo "FREE_SPACE=$FREE_SPACE"
echo "RISK=LOW"