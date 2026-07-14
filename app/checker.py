import subprocess
import re


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

    disk = run_shell("../modules/disk.sh")
    chrome = run_shell("../modules/chrome.sh")
    feishu = run_shell("../modules/feishu.sh")
    wechat = run_shell("../modules/wechat.sh")
    wps = run_shell("../modules/wps.sh")

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