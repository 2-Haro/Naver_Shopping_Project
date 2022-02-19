from selenium import webdriver
import time

# 네이버, 네이버 쇼핑 이동
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000") # chrome 창 사이즈 1000 * 1000
options.add_argument("no-sandbox") # 탭을 옮겨다니며 원하는 action, operation을 할 수 있게 한다
# options.add_argument("headless") # chrome 창이 뜨지 않게 한다

chrome = webdriver.Chrome("./chromedriver", options=options) 
chrome.get("https://naver.com") # get -> goto
chrome.get("https://shopping.naver.com")
chrome.back() # 뒤로 가기
chrome.forward() # 앞으로 가기
time.sleep(3)
chrome.close()