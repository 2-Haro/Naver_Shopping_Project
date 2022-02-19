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
login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#gnb_login_button"))).click() # 찾는 element가 보이는지(상호작용할 수 있는 상태인지)

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

search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=query]"))) # 검색창 찾기
search.send_keys("언더아머") # 검색창에 검색어 입력
time.sleep(1)
search.send_keys("\n") # 엔터

# selenium에서는 child 노드가 아닌 sibling 노드에 자유롭게 접근할 수 없으므로 공통된 parent 노드를 찾아서 접근한다
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^=basicList_info_area__"))) # basicList_info_area__로 시작하는 div 태그(상품 정보)의 존재 여부 확인

# 스크롤
for i in range(8):
  chrome.execute_script("window.scrollBy(0, " + str((i + 1) * 1000) + ")") # 스크롤을 끝까지 내리는 것을 여러 번 반복해서 document의 끝까지 가도록 한다
  time.sleep(1)
# chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)") # javascript를 selenium에게 실행하라고 명령 -> 스크롤을 끝까지 내려라
# document.body.scrollHeight: 현재 document 문서의 body 태그의 scroll로 내릴 수 있는 최대 높이 반환
# 해당 코드로는 정상적으로 document의 끝까지 갈 수 없다 -> 무한 스크롤 형태이기 때문에 스크롤을 내렸을 때 동적으로 계속해서 document의 길이를 늘리기 때문

items = chrome.find_elements_by_css_selector("div[class^=basicList_info_area__") # 해당하는 div 태그(상품 정보)를 전부 가져온다
for item in items:
  try:
    item.find_element_by_css_selector("button[class^=ad_]") # 광고
    continue
  except: # 광고 X
    pass
  print(item.find_element_by_css_selector("a[class^=basicList_link__]").text) # 광고가 아닌 상품 이름 가져오기

chrome.close()