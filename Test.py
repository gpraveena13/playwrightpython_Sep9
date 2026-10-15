from playwright.sync_api import sync_playwright

def Test_Sample():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False, slow_mo=3000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        # print(page.url)
        # print(page.title())
        # page.reload()
        # page.wait_for_timeout(3000)
        # page.get_by_placeholder("Enter Name").fill("praveena")
        # page.get_by_placeholder("Enter EMail").fill("p.g@gmail.com")
        # page.get_by_placeholder("Enter Phone").fill("1234567890")
        # page.locator("#textarea").fill("NewJersey")
        # page.locator("#textarea").scroll_into_view_if_needed()
        # page.get_by_text("Female").check()
        # page.locator("#male").check()
        # #page.wait_for_timeout(5000)
        # page.locator("//input[@id='tuesday']").check()
        # #page.wait_for_timeout(5000)
        # page.locator("#country").select_option("India")
        # #page.wait_for_timeout(5000)
        # page.locator("#country").scroll_into_view_if_needed()
        # page.locator("#colors").select_option(["Red","Green"])
        # page.locator("#colors").scroll_into_view_if_needed()
        # # page.wait_for_timeout(5000)
        # # page.locator("input.wikipedia-search-input").fill("selenium")
        # # page.locator("//input[@class='wikipedia-search-button']").click()
        # # page.wait_for_timeout(5000)
        # page.locator("input[type=\"submit\"]").click()
        # with page.expect_popup() as page1_info:
        #     page.get_by_role("link", name="Selenium", exact=True).click()
        #     page1 = page1_info.value
        #     page.locator('//*[@id="wikipedia-search-result-link"]/a').click()
        # # with context.new_page() as new_page_info:
        # #     page.get_by_text('newtab').click()
        # #     page2 = new_page_info.value 
        # #     print(page2.title())
        # #     print(page2.url)
            
        page.locator("//button[@name='start']").click()
        page.locator("//button[@name='stop']").click()
        page.wait_for_timeout(5000)
        //table[@name="BookTable"]//tr[2]/td[2]
                
      #  //*[@id="wikipedia-search-result-link"]/a
        
        
        
        
Test_Sample()