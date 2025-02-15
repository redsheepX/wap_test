if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.append(str(Path.cwd()))

from selenium import webdriver
from environment import emulator
from selenium.webdriver.chrome.options import Options


class wap_test:
    def __init__(self, device: str | None = None):
        if device is None:
            from random import choice

            device = choice(emulator().get_all_devices())
        mobile_emulation = {
            "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "clientHints": {"platform": "Mac", "mobile": False},
        }
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    def go_to_twitch(self):
        """go to twitch"""
        url = "https://www.twitch.tv/"
        # url = "https://www.whatismybrowser.com/"
        self.driver.get(url)
        while self.driver.execute_script("return document.readyState") != "complete":
            pass
        print(f"{url} is loaded")
        ...

    def open_driver(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def click_search_icom(self):
        self.driver.find_element_by_class_name(
            "LScInteractableBase-sc-ofisyf-0 ScInteractableDefault-sc-ofisyf-1 hGAIgs etibmD InjectLayout-sc-1i43xsx-0 iEupwg"
        ).click()


if __name__ == "__main__":
    a = wap_test()
    a.open_driver()
    a.go_to_twitch()
    a.click_search_icom()
