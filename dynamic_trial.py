#動態網頁爬蟲
import requests
from selenium import webdriver #可以模擬用戶在網站上載入、點擊等動作
from selenium.webdriver.common.by import By #用來定位元素
from selenium.webdriver.common.keys import Keys #用來導入按鍵
import time #python內建，用來暫時停止執行程式
"""
有些內容不能只看html，還需要用JavaScript跑才會出現
因此要用selenium模擬用戶加載、操作網頁來取得
"""


driver = webdriver.Chrome() #若py檔和webdriver.exe不在同一資料夾需在()中傳入絕對路徑
driver.get("https://hipala.github.io/js-example/") #前往指定網頁
driver.implicitly_wait(10) #給10秒等待下載網頁
print(driver.page_source) #顯示網頁原始碼
form = driver.find_element(By.TAG_NAME, "div") #搜尋第一個<div>#原始碼：<div id="word">JavaScript渲染才看得到這行</div>
print(form.tag_name) #輸出：div
print(form.get_attribute("id")) #輸出word (id="word")


#在搜尋框輸入
driver.get("https://www.google.com.tw/?hl=zh_TW") #chrome的頁面
driver.implicitly_wait(10)
element = driver.find_element(By.CLASS_NAME, "gLFyf") #因為chrome的搜索框是<textarea>，class是"gLFyf"，獲得其參考
element.send_keys("selenium") #在搜尋框中輸入selenium   
element.send_keys(Keys.ENTER) #按下按鍵

print(driver.page_source)
time.sleep(10) #停止程式10秒
driver.close() #關閉網頁