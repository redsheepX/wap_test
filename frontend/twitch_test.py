from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from selenium import webdriver
from environment import emulator
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from time import sleep


class Twitch_control:
    def __init__(self, device: str | None = None):
        if device is None:

            device = choice(emulator().get_all_devices())

        if isinstance(device, str):
            device = {"deviceName": device}

        self.device = device["deviceName"]
        # mobile_emulation = {
        #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        #     "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        #     "clientHints": {"platform": "Mac", "mobile": False},
        # }
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("mobileEmulation", device)

    def go_to_twitch(self, url="https://www.twitch.tv/"):
        """go to twitch"""
        # url = "https://www.twitch.tv/"
        url = "https://m.twitch.tv/directory"  # cause mobile web can't find search icon ,so change the website to this url
        # url = "https://www.whatismybrowser.com/"
        self.driver.get(url)
        print(f"{url} is loaded")

    def wait_page_loaded(self):
        while self.driver.execute_script("return document.readyState") != "complete":
            pass

    def open_driver(self):
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def click_icon(self):
        self.driver.find_element(By.XPATH, '//*[@id="twilight-sticky-header-root"]/div/div/div/div/input').click()

    def input_search_word(self, word):
        input_box = self.driver.find_element(By.XPATH, '//*[@id="twilight-sticky-header-root"]/div/div/div/div/input')
        input_box.send_keys(word)
        self.driver.find_element(By.XPATH, '//*[@id="page-main-content-wrapper"]/div/ul/li[1]/a').click()

    def scroll_down(self):
        for i in range(2):  # scroll down to buttom twice
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)

    def click_channels_tab(self):
        """cause search hone page can't scroll so i change it to channels page"""
        while True:
            try:
                self.driver.find_element(
                    By.XPATH, "/html/body/div[1]/main/nav/div/div[2]/div/ul/li[2]/a/div/div/div"
                ).click()
                break
            except Exception as E:
                pass
        self.wait_page_loaded()

    def click_streamer(self):
        wait = WebDriverWait(self.driver, 10)
        buttons = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@class, "ScCoreLink-sc-16kq0mq-0")]'))
        )
        visible_buttons = [button for button in buttons if button.is_displayed()]
        while True:
            try:
                self.random_choice_streamer(visible_buttons)  # FIXME sometimes has bug that cant find correct button
                break
            except:
                pass

    def random_choice_streamer(self, visible_buttons):
        random_streamer = choice(visible_buttons)
        random_streamer.click()

    def get_file_name(self, file_name=None):
        folder = Path("./screenshot/")
        folder.mkdir(parents=True, exist_ok=True)
        if file_name is None:
            import datetime

            file_name = self.device + str(datetime.date.today()) + ".png"
        return folder / file_name

    def save_screen_shot(self, file_name=None):

        while True:
            is_playing = self.driver.execute_script(
                """
            let video = document.querySelector('video');
            return video && !video.paused;
        """
            )
            if is_playing:
                sleep(1)  # wait 1 more sec
                break

        file_full_name = self.get_file_name(file_name)
        self.driver.save_screenshot(file_full_name)
