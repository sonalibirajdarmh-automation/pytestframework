import os
import time
from selenium import webdriver
import pytest
import os
from datetime import datetime

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain report object
#     outcome = yield
#     report = outcome.get_result()
#
#     # check if test failed
#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("driver")
#         if driver:
#             screenshots_dir = "screenshots"
#             os.makedirs(screenshots_dir, exist_ok=True)
#
#             timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             screenshot_path = f"{screenshots_dir}/{item.name}_{timestamp}.png"
#
#             driver.save_screenshot(screenshot_path)
#
#             # attach screenshot to html report
#             if hasattr(report, "extra"):
#                 import pytest_html
#                 report.extra.append(pytest_html.extras.image(screenshot_path))
#
#
#
# def pytest_configure(config):
#     reports_dir='reports'
#     os.makedirs(reports_dir, exist_ok=True)
#

@pytest.fixture(scope="session")
def driver():
    driver=webdriver.Chrome()
    driver.get("http://localhost:100")
    time.sleep(3)
    yield driver
    return driver