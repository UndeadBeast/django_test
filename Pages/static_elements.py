from selenium.webdriver.common.by import By


class MainPageElements(object):
    URL = "https://github.com/django/django"
    TITLE = "GitHub - django/django"


class MainPageLocators(object):
    LATEST_COMMIT_ISSUE_LINK = (By.CLASS_NAME, 'issue-link')
    LATEST_COMMIT_SHA = (By.CSS_SELECTOR, 'a.commit-tease-sha')


class CommitPageElements(object):
    URL = "https://github.com/django/django/commits/master"
    TITLE = "Commits · django/django · GitHub"


class CommitPageLocators(object):
    LAST_COMMIT_ID = (By.CSS_SELECTOR, 'div.commits-listing div.commit-links-cell a.sha')
