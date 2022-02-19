from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 입력한 시간 기준
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

chrome = webdriver.Chrome("./chromedriver", options=options)
chrome.get("https://shopping.naver.com") # selenium get 함수: 페이지 로딩을(일정 시간 - 완전히는 X) 기다려준다
# 완벽하게 페이지 로딩을 하기 위해서는 추가적인 코드 작성 필요
time.sleep(3) # 파이썬 프로그램이 멈춘다
chrome.implicitly_wait(3) # selenium, chromedriver, chrome이 멈춘다(통신하는 곳)
chrome.close()

# element의 browser 표시 여부 기준
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

chrome = webdriver.Chrome("./chromedriver", options=options)
chrome.get("https://shopping.naver.com") # selenium get 함수: 페이지 로딩을(일정 시간 - 완전히는 X) 기다려준다
# 완벽하게 페이지 로딩을 하기 위해서는 추가적인 코드 작성 필요
# 표시되길 원하는 element(네이버 쇼핑 검색창)의 browser 표시 여부를 기준
WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
# input 태그 내의 name attribute가 query인 CSS 선택자(검색창)가 로딩이 될 때까지 최대 10초 동안 chrome 브라우저가 기다린다
chrome.close()