# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url ='http://localhost:7000/#!/panel'

# keyword
chrome_options = Options()
chrome_options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
num = driver.find_element_by_id("app").text
print(num)

now_handle = driver.current_window_handle
#Click the button, Open a New window for English version
driver.find_element_by_class_name("btn").click()
#Get the handle information from all windows
all_handles = driver.window_handles
for handle in all_handles:
    #check the new window handle
    if handle != now_handle:
        print(handle)
      #Use the new window, band with it
        driver.switch_to.window(handle)
        num1 = driver.find_element_by_id("id").text
        print(num1)
        time.sleep(2)
        driver.close()

time.sleep(2)
driver.quit()





