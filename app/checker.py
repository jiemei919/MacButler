import subprocess
import re
import os


def run_shell(path):
    result = subprocess.run(
        [path],
        capture_output=True,
        text=True
    )
    return result.stdout


def get_value(text, key):
    match = re.search(rf"{key}=(.*)", text)
    if match:
        return match.group(1).strip()
    return ""


def run_check():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    modules_dir = os.path.join(base_dir, "modules")

    disk = run_shell(os.path.join(modules_dir, "disk.sh"))
    chrome = run_shell(os.path.join(modules_dir, "chrome.sh"))
    feishu = run_shell(os.path.join(modules_dir, "feishu.sh"))
    wechat = run_shell(os.path.join(modules_dir, "wechat.sh"))
    wps = run_shell(os.path.join(modules_dir, "wps.sh"))

    return {

        "disk": {
            "free": get_value(disk, "FREE_SPACE"),
            "risk": get_value(disk, "RISK")
        },

        "chrome": {
            "cache": get_value(chrome, "CACHE_SIZE"),
            "risk": get_value(chrome, "RISK")
        },

        "feishu": {
            "data": get_value(feishu, "DATA_SIZE"),
            "risk": get_value(feishu, "RISK")
        },

        "wechat": {
            "data": get_value(wechat, "DATA_SIZE"),
            "risk": get_value(wechat, "RISK")
        },

        "wps": {
            "data": get_value(wps, "DATA_SIZE"),
            "risk": get_value(wps, "RISK")
        }

    }