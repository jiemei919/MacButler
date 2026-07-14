import subprocess
from checker import run_check


report = run_check()


subprocess.run(
    [
        "osascript",
        "-e",
        f'display dialog "{report}" with title "MAC 管家体检结果" buttons {{"关闭"}} default button "关闭"'
    ]
)