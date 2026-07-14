import subprocess

print("================================")
print("        MAC 管家 V1")
print("================================")
print()

modules = [
    "../modules/disk.sh",
    "../modules/chrome.sh",
    "../modules/feishu.sh",
    "../modules/wechat.sh",
]

for module in modules:
    subprocess.run([module])
    print()