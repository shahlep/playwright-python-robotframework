from playwright.sync_api import sync_playwright

#with sync_playwright() as p:
p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://demo.seleniumeasy.com/")
page.screenshot(path="example.png")
browser.close()

p.stop()