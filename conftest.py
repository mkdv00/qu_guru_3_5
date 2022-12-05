import pytest
from selene import have, command
from selene.support.shared import browser


@pytest.fixture
def open_browser():
    browser.config.timeout = 3.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/automation-practice-form')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    ads.should(have.size_less_than_or_equal(3))
    ads.perform(command.js.remove)
    yield
    browser.quit()
