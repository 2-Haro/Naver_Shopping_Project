from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com")
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click()

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

pyperclip.copy("ID")
input_id.send_keys(Keys.CONTROL, 'v') # Windows
# input_id.send_keys(Keys.COMMAND, 'v') # Mac

pyperclip.copy("PASSWORD")
input_pw.send_keys(Keys.CONTROL, 'v') # Windows
# input_pw.send_keys(Keys.COMMAND, 'v') # Mac
input_pw.send_keys("\n")

short_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button")))

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=query]")))
search.send_keys("언더아머")
time.sleep(1)
search.send_keys("\n")

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class^=basicList_link__]")))
product = chrome.find_elements_by_css_selector("a[class^=basicList_link__]")
product[1].click() # 두번째 상품 클릭

time.sleep(2)

chrome.switch_to.window(chrome.window_handles[1])

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[aria-haspopup='listbox']"))) # 옵션의 존재 여부 확인
options = chrome.find_elements_by_css_selector("a[aria-haspopup='listbox']") # 옵션 정보를 전부 가져온다(리스트)

options[0].click() # 첫번째 옵션 클릭
time.sleep(0.1)
chrome.find_element_by_css_selector("ul[role=listbox] a[role=option]").click() # 첫번째 옵션의 첫번째 항목 클릭
# chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(2) a[role=option]").click() # 첫번째 옵션의 두번째 항목 클릭
# chrome.find_element_by_css_selector("ul[role=listbox] a[role=option]")[1].click() # 첫번째 옵션의 두번째 항목 클릭

options[1].click() # 두번째 옵션 클릭
time.sleep(0.1)
chrome.find_element_by_css_selector("ul[role=listbox] li:nth-child(4) a[role=option]").click() # 두번째 옵션의 네번째 항목 클릭

chrome.find_element_by_css_selector("div[class*='N=a:pcs.buy'] a").click() # 구매하기 버튼 누르기

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button._doPayButton"))).click() # 결제하기 버튼 누르기

chrome.quit()