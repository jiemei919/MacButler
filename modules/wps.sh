#!/bin/bash

echo "=============================="
echo "📄 WPS"
echo "=============================="

cache=$(du -sh ~/Library/Containers/com.kingsoft.wpsoffice.mac/Data/Library/Caches 2>/dev/null | awk '{print $1}')
support=$(du -sh ~/Library/Containers/com.kingsoft.wpsoffice.mac/Data/Library/Application\ Support 2>/dev/null | awk '{print $1}')

echo "缓存大小：$cache"
echo "数据占用：$support"
echo "风险等级：🟡 数据请勿直接删除"
echo "建议：优先使用 WPS 自带『缓存清理』或『云文档管理』功能。"