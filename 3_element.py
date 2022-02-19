from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Element Search
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

chrome = webdriver.Chrome("./chromedriver", options=options)
chrome.get("https://shopping.naver.com")
time.sleep(3)
# css selector 기반 Search
el = chrome.find_element_by_css_selector("input[name=query]")
print(el)
chrome.close()

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

chrome = webdriver.Chrome("./chromedriver", options=options)
chrome.get("https://shopping.naver.com")
wait = WebDriverWait(chrome, 10)
# css selector 기반 Search
el = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[name=query]")))
print(el)
chrome.close()

# Element Click
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

chrome = webdriver.Chrome("./chromedriver", options=options)
chrome.get("https://shopping.naver.com")
wait = WebDriverWait(chrome, 10)

def find(wait, css_selector): # Element를 찾는 함수(css selector 기반)
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "input[name=query]") # 검색창
search.send_keys("언더아머") # 검색어 타이핑(텍스트 타이핑)

time.sleep(3)

button = find(wait, "a.co_srh_btn") # 검색 버튼
button.click() # 검색 버튼 클릭

time.sleep(3)

chrome.close()

# Element Enter
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
# options.add_argument("headless")

chrome = webdriver.Chrome("./chromedriver", options=options)
chrome.get("https://shopping.naver.com")
wait = WebDriverWait(chrome, 10)

def find(wait, css_selector): # Element를 찾는 함수(css selector 기반)
  return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "input[name=query]") # 검색창
search.send_keys("언더아머\n") # 검색어 타이핑(텍스트 타이핑), Enter(새로운 줄 입력)

time.sleep(3)

chrome.close()