#!/bin/bash

echo "📀 磁盘检查"

diskutil info / | grep "Container Free Space"