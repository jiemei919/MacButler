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
    "../modules/wps.sh",
]

for module in modules:
    subprocess.run([module])
    print()

print("================================")
print("📋 MAC 管家体检总结")
print("================================")
print()

print("本次检查：")
print()
print("🔴 Chrome")
print("缓存过大，建议尽快清理。")
print()
print("🟡 飞书")
print("数据占用较大，请勿直接删除数据。")
print()
print("🟡 微信")
print("缓存可以清理，数据请勿直接删除。")
print()
print("🟡 WPS")
print("数据占用较大，请勿直接删除数据。")
print()
print("--------------------------------")
print()
print("总体建议：")
print()
print("① 优先清理 Chrome 缓存")
print("② 使用飞书自带存储空间清理")
print("③ 使用微信存储空间管理")
print("④ 使用 WPS 自带缓存清理")
print()
print("================================")
print("体检完成")
print("================================")