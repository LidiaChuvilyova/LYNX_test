import os
from datetime import datetime
import time

import pytest
from selenium import webdriver
import chromedriver_autoinstaller


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    timestamp = datetime.now().strftime('%H-%M-%S')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        feature_request = item.funcargs['request']
        # get browser from fixture
        for i in range(0, len(feature_request.fixturenames)):
            if 'browser' in feature_request.fixturenames[i]:
                frBrowser = feature_request.fixturenames[i]
                break
        driver = feature_request.getfixturevalue(frBrowser)

        if report.failed:
            screenshotDir = os.path.dirname(__file__) + "\\Logs"
            if not os.path.exists(screenshotDir):
                os.makedirs(screenshotDir)
            screenshotPath = screenshotDir + "\\src" + timestamp + '.png'
            time.sleep(1)
            driver.save_screenshot(screenshotPath)
            print("save screen: " + screenshotPath)

            extra.append(pytest_html.extras.image(screenshotPath))
            extra.append(pytest_html.extras.url(driver.current_url))

        report.extra = extra


@pytest.fixture(scope="function")
def browser(request):
    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
    # and if it doesn't exist, download it automatically,
    # then add chromedriver to path

    print("\nstart browser for test..")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--window-size=1920,1080")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()
