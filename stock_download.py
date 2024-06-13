from selenium import webdriver #可以模擬用戶在網站上載入、點擊等動作
from selenium.webdriver.common.by import By #用來定位元素
from selenium.webdriver.common.keys import Keys #用來導入按鍵
import time

import move_file #自製，用來移動檔案

#偽裝headers
user_agent = "Mozilla/5.0"
opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
opt.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation']) #禁止輸出日誌（不然console很亂）
opt.add_argument('disable-gpu')
opt.add_argument('log-level=3') #多少等級的訊息才會輸出到console：INFO=0 WARNING=1 LOG_ERROR=2 LOG_FATAL=3

driver = webdriver.Chrome(options=opt)
driver.get("https://finance.yahoo.com/") #開啟yahoo finance
driver.implicitly_wait(3) #騰出5秒讓網頁載好

#處理輸入
num_stock = int(input("輸入想查詢的股票數量："))
stock_symbol = [] #儲存輸入
while(len(stock_symbol) < num_stock): #持續詢問直到
    tmps = input("輸入想查詢的四碼股票代號（代號間以空白分隔）：").split() 
    for tmp in tmps:
        stock_symbol.append(tmp)
    if len(stock_symbol) < num_stock:
        print(f"還剩{num_stock-len(stock_symbol)}檔，目前已指定：{stock_symbol}")


for i in range(num_stock):
    print(f"當前抓取進度：{i+1}/{num_stock}")
    inputElement = driver.find_element(By.TAG_NAME, "input") #獲得輸入框的參考（第一個input就是搜尋框）
    inputElement.send_keys(stock_symbol[i]+".TW") #輸入股票代碼
    time.sleep(0.5)
    inputElement.submit() #送出查詢
    driver.implicitly_wait(5)
    driver.get(driver.current_url+"history/") #跳轉到該檔股票的股價歷史頁面
    driver.implicitly_wait(5)

    #time.sleep(100)#

    arrow = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/div[2]/div[1]/div[1]/button') #這是日期選單的箭頭，路徑是.dataRangeBtn>div>span
    arrow.click() #點擊展開日期選單         //*[@id=\"Col1-1-HistoricalDataTable-Proxy\"]/section/div[1]/div[1]/div[1]/div/div/div/svg #google跟webdriver開出來頁面的HTML不一樣，以webdriver為準
    time.sleep(1)                         
    periods = driver.find_elements(By.CSS_SELECTOR, '.quickpicks button') #獲得時間長度按鈕的list
    for period in periods:
        if period.text == "5Y": 
            period.click() #找需要的那個時間
            break #按下5Y之後清單會消失，故無法訪問剩下元素，不break的話會爛掉

    driver.implicitly_wait(5)
    download = driver.find_element(By.XPATH, '//*[@id="nimbus-app"]/section/section/section/article/div[2]/div[2]/div/a/span') #下載按鈕
    download.click()
    time.sleep(2) #避免沒載完就close()
driver.close()

move_file.move_file(r"C:\Users\Joy\Downloads\*.TW.csv", r"C:\Codes\Python\WebCrawler\csv") #把下載的.csv移至指定的資料夾