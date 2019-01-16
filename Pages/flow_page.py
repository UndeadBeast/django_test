# import time

from Pages.static_elements import CommitPageLocators,CommitPageElements


class CommitPage(object):

    def __init__(self, driver_come, default_wait_timeout=30):
        self.driver = driver_come
        self.default_wait_timeout = default_wait_timeout
        # time.sleep(2)

    #   -------------------------------------------------------------------

    def switch_to_master_commit_page(self):
        self.driver.get(CommitPageElements.URL)

    def is_title_exists(self):
        return CommitPageElements.TITLE in self.driver.title

    def get_latest_commit_id(self):
        self.switch_to_master_commit_page()
        assert self.is_title_exists(), "Can't load page or title not as expected"
        commit_sha_link = self.driver.find_element(*CommitPageLocators.LAST_COMMIT_ID).text
        return commit_sha_link

    #   -------------------------------------------------------------------

    def destroy(self):
        self.driver.quit()
