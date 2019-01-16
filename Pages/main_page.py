# import time

from Pages.static_elements import MainPageLocators, MainPageElements


class MainPage(object):

    def __init__(self, driver_come, default_wait_timeout=30):
        self.driver = driver_come
        self.default_wait_timeout = default_wait_timeout
        # time.sleep(2)

    #   -------------------------------------------------------------------

    def switch_to_main_page(self):
        self.driver.get(MainPageElements.URL)

    def is_title_exists(self):
        return MainPageElements.TITLE in self.driver.title

    def get_latest_commit_id(self):
        self.switch_to_main_page()
        assert self.is_title_exists(), "Can't load page or title not as expected"
        latest_commit_sha = self.driver.find_element(*MainPageLocators.LATEST_COMMIT_SHA)
        assert latest_commit_sha.is_displayed(), "No _latest commit SHA_ visible on the main page"
        return latest_commit_sha.text

    #   -------------------------------------------------------------------

    def destroy(self):
        self.driver.quit()
