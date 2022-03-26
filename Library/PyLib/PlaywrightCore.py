from playwright.sync_api import sync_playwright


class PlaywrightCore:
    browser = None
    context = None
    page = None
    pwSync = None

    @staticmethod
    def launch_browser(browser_name):
        print("Opening browser : "+browser_name)
        PlaywrightCore.pwSync = sync_playwright().start()
        if browser_name.lower() == 'chromium':
            PlaywrightCore.browser = PlaywrightCore.pwSync.chromium.launch(headless=False, slow_mo=1000)
        elif browser_name.lower() == 'firefox':
            PlaywrightCore.browser = PlaywrightCore.pwSync.firefox.launch(headless=False, slow_mo=1000)
        else:
            PlaywrightCore.browser = PlaywrightCore.pwSync.webkit.launch(headless=False, slow_mo=1000)

        PlaywrightCore.context = PlaywrightCore.browser.new_context()

    @staticmethod
    def close_browser():
        PlaywrightCore.context.close()
        PlaywrightCore.browser.close()
        PlaywrightCore.pwSync.stop()

    @staticmethod
    def open_application():
        PlaywrightCore.page = PlaywrightCore.context.new_page()
        PlaywrightCore.page.goto('https://demo.seleniumeasy.com/')
        if PlaywrightCore.page.query_selector("text=No, thanks!"):
            PlaywrightCore.page.click("text=No, thanks!")

    @staticmethod
    def close_application():
        PlaywrightCore.page.close()

    @staticmethod
    def get_page_object():
        return PlaywrightCore.page

    @staticmethod
    def take_screenshot():
        return PlaywrightCore.page.screenshot(path='example.png')
