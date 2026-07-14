import rumps
from checker import run_check


def risk_icon(risk):
    if risk == "HIGH":
        return "🔴"
    elif risk == "MEDIUM":
        return "🟡"
    elif risk == "LOW":
        return "🟢"
    else:
        return "⚪"


class MacButler(rumps.App):

    def __init__(self):
        super().__init__(
            "🔧 MAC管家",
            quit_button=None
        )

        # 创建菜单（只创建一次）
        self.disk_item = rumps.MenuItem("")
        self.chrome_item = rumps.MenuItem("")
        self.feishu_item = rumps.MenuItem("")
        self.wechat_item = rumps.MenuItem("")
        self.wps_item = rumps.MenuItem("")

        self.menu = [
            self.disk_item,
            self.chrome_item,
            self.feishu_item,
            self.wechat_item,
            self.wps_item,
            None,
            "🔄 刷新",
            None,
            "退出"
        ]

        self.load_menu()

    def load_menu(self):
        result = run_check()

        self.disk_item.title = (
            f"📀 磁盘剩余：{result['disk']['free']} {risk_icon(result['disk']['risk'])}"
        )

        self.chrome_item.title = (
            f"🌐 Chrome：{result['chrome']['cache']} {risk_icon(result['chrome']['risk'])}"
        )

        self.feishu_item.title = (
            f"📘 飞书：{result['feishu']['data']} {risk_icon(result['feishu']['risk'])}"
        )

        self.wechat_item.title = (
            f"💬 微信：{result['wechat']['data']} {risk_icon(result['wechat']['risk'])}"
        )

        self.wps_item.title = (
            f"📄 WPS：{result['wps']['data']} {risk_icon(result['wps']['risk'])}"
        )

    @rumps.clicked("🔄 刷新")
    def refresh(self, _):
        self.load_menu()

        rumps.notification(
            "MAC 管家",
            "",
            "体检完成"
        )

    @rumps.clicked("退出")
    def quit(self, _):
        rumps.quit_application()


if __name__ == "__main__":
    MacButler().run()