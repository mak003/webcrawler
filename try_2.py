# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url ='http://localhost:7000/#!/panel'

# Open Chrome
chrome_options = Options()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
num = driver.find_element_by_id("app").text
print(num)

#Window handles
now_handle = driver.current_window_handle
#Click the button, Open a New window for English version
driver.find_element_by_class_name("btn").click()
#Get the handle information from all windows
all_handles = driver.window_handles
for handle in all_handles:
    #Check the new window's handle
    if handle != now_handle:
        print(handle)
      #Use the new window, band with it
        driver.switch_to.window(handle)
        num1 = driver.find_element_by_id("id").text
        print(num1)
        time.sleep(2)
        driver.close()

"""    
#From Edmund Martin's blog
def get_page(self.url):
    try:
        self.browser.get(url)
        return self.browser.page_source
    except Exception as e:
        logging.exception(e)
        return

#From Jingmi's blog    
def main()
    MAX_PAGE = 100
    for i in range(1, MAX_PAGE + 1):
        index_page(1)
    browser.close()
"""

time.sleep(2)
driver.quit()





