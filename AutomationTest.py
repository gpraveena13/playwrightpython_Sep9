from playright.sync_api import sync_playwright

def AutomationTest():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slo_mo=3000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        print(page.url)
        print(page.title())
        page.reload()
        
        