#!/bin/bash

echo "=============================="
echo "📘 飞书"
echo "=============================="

cache=$(du -sh ~/Library/Containers/com.bytedance.macos.feishu/Data/Library/Caches 2>/dev/null | awk '{print $1}')
support=$(du -sh ~/Library/Containers/com.bytedance.macos.feishu/Data/Library/Application\ Support 2>/dev/null | awk '{print $1}')

echo "缓存大小：$cache"
echo "数据占用：$support"
echo "风险等级：🟢 缓存可清理 / 🟡 数据请勿直接删除"
echo "建议：优先使用飞书自带『存储空间清理』功能。"