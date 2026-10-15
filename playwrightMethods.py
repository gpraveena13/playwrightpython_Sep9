from playwright.sync_api import sync_playwright

#p=sync_playwright().start()  # start playwirght engine
# #browser = p.chromium.launch(headless=False)  # browser
# #context =browser.new_context()   #window/session/context
# page =context.new_page()  #tab/page
# page1 =context.new_page()
# context2 = browser.new_context()
# page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  #
# page.wait_for_timeout(15000)
# p.stop()

def locators():
	with sync_playwright() as p:
		browser = p.chromium.launch(headless=False,slow_mo=5000)  # browser
		context =browser.new_context()   #window/session/context
		page =context.new_page()  #tab/page
		#page1 =context.new_page()
		#context2 = browser.new_context()
		page.goto("https://testautomationpractice.blogspot.com/")  #
	#	page.wait_for_timeout(15000)
		page.reload()
		print(page.title())
		print(page.url)
		# page.get_by_placeholder("Enter Name").fill("praveena")
		# page.get_by_role("radio", name="Female").check()
		# #page.wait_for_timeout(3000)
		# page.get_by_role("radio", name="Male").nth(0).check()
		# #page.wait_for_timeout(3000)
		# page.get_by_label("Address:").fill("address")
		# page.get_by_text('Slider').scroll_into_view_if_needed()
		# page.locator("//input[@id='phone']").fill("123456789")
		# #page.wait_for_timeout(3000)
		# page.locator("//input[@class='form-control']").nth(0).fill('testurlplaywright@gmail.com')
		#page.wait_for_timeout(3000)
		page.locator("//*[@id='Wikipedia1_wikipedia-search-input']").fill('TESTrun')
		page.locator("//*[contains(text(),'Confirmation Alert')]").click()
		
  
  #("//button[@id='alertBtn']/ancestor::h2[@class='title']")
  
# //input[@class='a-button-input']/ancestor::div[@data-csa-c-item-id="B0HJ9W3ZND"]


locators() 


# //*[@id="phone"]

# //*[@id="email"]

# <input class="wikipedia-search-input" id="Wikipedia1_wikipedia-search-input" type="text">

//*[@id="datepicker"]