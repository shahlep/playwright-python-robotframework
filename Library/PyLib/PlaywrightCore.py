from playwright.sync_api import sync_playwright
from robot.api.deco import library, keyword


@library
class PlaywrightCore:
    browser = None
    context = None
    page = None
    pwSync = None

    @keyword
    def launch_browser(self, browser_name):
        print("Opening browser : " + browser_name)
        PlaywrightCore.pwSync = sync_playwright().start()
        if browser_name.lower() == 'chromium':
            PlaywrightCore.browser = PlaywrightCore.pwSync.chromium.launch(headless=True, slow_mo=1000)
        elif browser_name.lower() == 'firefox':
            PlaywrightCore.browser = PlaywrightCore.pwSync.firefox.launch(headless=True, slow_mo=1000)
        else:
            PlaywrightCore.browser = PlaywrightCore.pwSync.webkit.launch(headless=True, timeout=6000)

        PlaywrightCore.context = PlaywrightCore.browser.new_context()

    @keyword
    def close_browser(self):
        PlaywrightCore.context.close()
        PlaywrightCore.browser.close()
        PlaywrightCore.pwSync.stop()

    @keyword
    def open_application(self):
        PlaywrightCore.page = PlaywrightCore.context.new_page()
        PlaywrightCore.page.goto('https://demo.seleniumeasy.com/')
        if PlaywrightCore.page.query_selector("text=No, thanks!"):
            PlaywrightCore.page.click("text=No, thanks!")

    @keyword
    def close_application(self):
        PlaywrightCore.page.close()

    @keyword
    def get_page_object(self):
        return PlaywrightCore.page

    @keyword
    def take_screenshot(self):
        return PlaywrightCore.page.screenshot(path='example.png')
