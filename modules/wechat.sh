#!/bin/bash

DOCS=$(du -sh ~/Library/Containers/com.tencent.xinWeChat/Data/Documents 2>/dev/null | awk '{print $1}')
FILES=$(du -sh ~/Library/Containers/com.tencent.xinWeChat/Data/Documents/xwechat_files 2>/dev/null | awk '{print $1}')
APP=$(du -sh ~/Library/Containers/com.tencent.xinWeChat/Data/Documents/app_data 2>/dev/null | awk '{print $1}')

echo "DATA_SIZE=$DOCS"
echo "FILES_SIZE=$FILES"
echo "APPDATA_SIZE=$APP"
echo "RISK=MEDIUM"