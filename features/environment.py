from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

_BROWSERS = {
    'chrome': lambda: webdriver.Chrome(ChromeDriverManager().install()),
    'firefox': lambda: webdriver.Firefox(executable_path=GeckoDriverManager().install()),
    'edge': lambda: webdriver.Edge(EdgeChromiumDriverManager().install())
}


def before_all(context):
    try:
        browser = context.config.userdata['browser']
    except (KeyError, AttributeError):
        raise RuntimeError(
            f'A browser has not been set. Please define a browser as one of the following: {list(_BROWSERS.keys())}')
    context.get_browser_driver = _BROWSERS[browser]


def before_scenario(context, scenario):
    try:
        context.driver = context.get_browser_driver()
    except WebDriverException:
        pass


def after_scenario(context, scenario):
    context.driver.quit()
