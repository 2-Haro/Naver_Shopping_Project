from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyperclip # 파이썬에서 클립보드를 활용할 수 있는 라이브러리

# 로그인 페이지 이동
chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome, 10) # element가 로딩될 때까지 최대 10초 동안 기다린다
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com")
# login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))) # 찾는 element가 존재하는지
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))) # 찾는 element가 보이는지(상호작용할 수 있는 상태)
print(login_button.text)
login_button.click()

time.sleep(3)

chrome.close()

# 로그인
chrome = webdriver.Chrome("./chromedriver")
wait = WebDriverWait(chrome, 10) # element가 로딩될 때까지 최대 10초 동안 기다린다
short_wait = WebDriverWait(chrome, 3)

chrome.get("https://shopping.naver.com")
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click() # 찾는 element가 보이는지(상호작용할 수 있는 상태인지)

input_id = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#id")))
input_pw = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#pw")))

pyperclip.copy("ID") # 클립보드에 ID 복사
input_id.send_keys(Keys.CONTROL, 'v') # Windows
# input_id.send_keys(Keys.COMMAND, 'v') # Mac

pyperclip.copy("PASSWORD") # 클립보드에 Password 복사
input_pw.send_keys(Keys.CONTROL, 'v') # Windows
# input_pw.send_keys(Keys.COMMAND, 'v') # Mac
input_pw.send_keys("\n")

# input_id.send_keys("ID") # 자동 입력 방지
# input_pw.send_keys("PASSWORD\n") # 자동 입력 방지

short_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#gnb_logout_button"))) # 로그아웃 버튼의 존재 여부로 로그인 여부 확인

chrome.close()