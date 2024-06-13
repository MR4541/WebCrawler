from selenium import webdriver #可以模擬用戶在網站上載入、點擊等動作
from selenium.webdriver.common.by import By #用來定位元素
from selenium.webdriver.common.keys import Keys #用來導入按鍵
import time

def print_price(n, v,o,h,l, lt,lz,ld,lp,lv): #格式化輸出
    print(n.text[5:])
    print(f"總成交量：{v.text}\n開盤價：{o.text}\n當日最高/最低價：{h.text}/{l.text}")
    print(f"最近一筆交易：\n成交時間：{lt.text} ｜ 成交價：{lz.text} ｜ 單量：{lv.text} ｜ 漲跌：{ld.text[1:]}{lp.text}")

stock_symbol = input("輸入四碼股票代號：") #type: str
driver = webdriver.Chrome()
target_url = "https://mis.twse.com.tw/stock/fibest.jsp?stock=" + stock_symbol +"&lang=zh_tw" 
driver.get(target_url) #前往目標網址
#抓數據
name = driver.find_element(By.ID, stock_symbol+"_n") #代號和公司名
volume = driver.find_element(By.ID, stock_symbol+"_v") #當日總成交量
open_price = driver.find_element(By.ID, stock_symbol+"_o") #開盤價
highest_price = driver.find_element(By.ID, stock_symbol+"_h") #當日最高價
lowest_price = driver.find_element(By.ID, stock_symbol+"_l") #當日最低價
latest_time = driver.find_element(By.ID, stock_symbol+"_t") #最近一筆成交時間
latest_price = driver.find_element(By.ID, stock_symbol+"_z") #最近一筆成交價
latest_diff = driver.find_element(By.ID, stock_symbol+"_diff") #最近一筆漲跌值
latest_pre = driver.find_element(By.ID, stock_symbol+"_pre") #最近一筆漲跌百分比
latest_volume = driver.find_element(By.ID, stock_symbol+"_tv") #最近一筆單量

print_price(name, volume, open_price, highest_price, lowest_price, latest_time, latest_price, latest_diff, latest_pre, latest_volume)


driver.close() #關閉網頁