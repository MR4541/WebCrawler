import requests #檔案名稱不可以跟套件一樣，電腦會不知道你在import誰
from bs4 import BeautifulSoup #用來分析HTML

url = "https://mr.ckeisc.org/" #要抓取的網址
headers = {"user-agent":"Mozilla/5.0"} #偽裝成指定headers
r = requests.get(url=url, headers=headers) #回傳一個response物件
print(r.text) #返回網頁原始碼
print(r.status_code) #返回狀態碼（200）
print(r.headers) #返回headers\

soup = BeautifulSoup(r.text, 'html.parser') #傳入原始碼和解析方式
print(soup.prettify()) #輸出排版過的原始碼
print(soup.div) #只輸出包含標籤<div>的部分
print(soup.find_all('a', limit=2))#尋找頭兩個<a>標籤，回傳bs4.element.tag組成的陣列
print(soup.find("p", class_="text")) #回傳第一個有class="text"的<p>

#取得網站中所有的超連結
for i in soup.find_all('a'):
    href = i.get("href") #輸出"href"=的東西 #type: str
    if href[0:5] == "https": 
        print(i.getText()) #輸出<a></a>內夾的文字
        print(href) 