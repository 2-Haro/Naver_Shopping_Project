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

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[class^=basicList_link__]"))).click() # 상품 클릭

time.sleep(2)

# print(chrome.window_handles) # window(탭)의 id(리스트)
# chrome.window_handles[0] # 먼저 열린 탭 -> 검색 결과 탭
# chrome.window_handles[1] # 나중에 열린 탭 -> 상품 페이지

chrome.switch_to.window(chrome.window_handles[1]) # 상품 페이지 탭으로 이동

chrome.quit() # 모든 chrome 브라우저(탭) 종료