# step1 go to twitch
# step2 click in search icon
# step3 input "StarCraft II"
# step4 scroll down 2 times
# step5 select streamer
# step6 on the streamer page wait until all is loaded and take a screenshot

from frontend.twitch_test import Twitch_control
import pytest
from pathlib import Path


@pytest.fixture(scope="class")
def driver(device=None):
    return Twitch_control(device)


class Test_twitch_wap:
    def test_open_twitch(self, driver: Twitch_control):
        driver.open_driver()
        driver.go_to_twitch()
        driver.click_icon()
        driver.input_search_word("StarCraft II")
        driver.click_channels_tab()
        driver.scroll_down()
        driver.click_streamer()
        file_full_name = driver.get_file_name()
        driver.save_screen_shot()
        assert Path(file_full_name).is_file(), "screenshot fail"
