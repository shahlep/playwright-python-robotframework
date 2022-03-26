from playwright.sync_api import sync_playwright

#with sync_playwright() as p:
p = sync_playwright().start()

#device emulation with aspect ratio
#device = p.devices['iPhone 11']
browser = p.chromium.launch(headless=False, slow_mo=1000)
context = browser.new_context(
    viewport={'width': 760, 'height': 630}
)
#context.tracing.start(screenshots=True,snapshots=True)
page = context.new_page()

page.goto("https://demo.seleniumeasy.com/")
page.screenshot(path="example.png")

#page.pause()
# Click text=No, thanks!
page.locator("text=No, thanks!").click()
# Click #treemenu >> text=Input Forms
page.locator("#treemenu >> text=Input Forms").click()
# Click #treemenu >> text=Simple Form Demo
page.locator("#treemenu >> text=Simple Form Demo").click()
# expect(page).to_have_url("https://demo.seleniumeasy.com/basic-first-form-demo.html")
# Click [placeholder="Please enter your Message"]
page.locator("[placeholder=\"Please enter your Message\"]").click()
# Fill [placeholder="Please enter your Message"]
page.locator("[placeholder=\"Please enter your Message\"]").fill("test msg")
# Click button:has-text("Show Message")
page.locator("button:has-text(\"Show Message\")").click()

#context.tracing.stop(path="trace.zip")      #playwright show-trace trace.zip
page.close()
context.close()
browser.close()

p.stop()