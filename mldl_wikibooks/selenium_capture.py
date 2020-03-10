from selenium import webdriver

url="http://www.naver.com"

browser=webdriver
browser.implicitly_wait(3)
browser.get(url)
browser.save_screenshot('website.png')
browser.quit()