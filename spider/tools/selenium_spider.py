from pyvirtualdisplay import Display
from selenium import webdriver
from scrapy.selector import Selector
browser = webdriver.Chrome()
browser.get('https://www.lagou.com/jobs/6451642.html?show=ef1d7810e9e0498db128f17a11c896f4')
# print(browser.page_source)

selector = Selector(text=browser.page_source)

print(selector.css(".job_request .salary::text").extract())

chrome_settings = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_settings.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_settings)
browser.get('https://www.lagou.com/jobs/6451642.html?show=ef1d7810e9e0498db128f17a11c896f4')

display = Display(visible=0, size=(800, 600))
display.start()

chrome_settings = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_settings.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_settings)
browser.get('https://www.lagou.com/jobs/6451642.html?show=ef1d7810e9e0498db128f17a11c896f4')

browser.quit()

