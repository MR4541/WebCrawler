from selenium import webdriver #可以模擬用戶在網站上載入、點擊等動作
from selenium.webdriver.common.by import By #用來定位元素
from selenium.webdriver.common.keys import Keys #用來導入按鍵
import time
import requests
import os

r = requests.get('https://mr.ckeisc.org')
print(os.path.basename(r"C:\Users\Joy\Downloads\1101.TW.csv"))
