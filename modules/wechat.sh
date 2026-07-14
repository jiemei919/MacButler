#!/bin/bash

echo "=============================="
echo "💬 微信"
echo "=============================="

cache=$(du -sh ~/Library/Containers/com.tencent.xinWeChat/Data/Library/Caches 2>/dev/null | awk '{print $1}')
support=$(du -sh ~/Library/Containers/com.tencent.xinWeChat/Data/Library/Application\ Support 2>/dev/null | awk '{print $1}')

echo "缓存大小：$cache"
echo "数据占用：$support"
echo "风险等级：🟢 缓存可清理 / 🟡 数据请勿直接删除"
echo "建议：优先使用微信自带『存储空间管理』功能。"