#!/bin/bash

echo "=============================="
echo "🌐 Chrome"
echo "=============================="

CHROME="$HOME/Library/Application Support/Google/Chrome/Default"

if [ ! -d "$CHROME" ]; then
    echo "状态：❌ 未安装 Chrome"
    exit
fi

SIZE=$(du -sh "$CHROME/Service Worker" 2>/dev/null | awk '{print $1}')
NUM=$(echo "$SIZE" | sed 's/G//')

echo "缓存大小：$SIZE"

if (( $(echo "$NUM > 5" | bc -l) )); then
    echo "风险等级：🔴 高"
    echo "原因：Chrome Service Worker 缓存超过 5GB。"
    echo "建议：优先使用 Chrome 自带『清除浏览数据』功能。"
else
    echo "风险等级：🟢 低"
    echo "原因：缓存大小正常。"
fi