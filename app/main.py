import subprocess

print("================================")
print("        MAC 管家 V1")
print("================================")
print()

modules = [
    "../modules/disk.sh",
    "../modules/chrome.sh",
]

for module in modules:
    subprocess.run([module])
    print()