import glob
import os
import csv #用作.csv檔案處理
import pandas as pd #做表格數據處理
import matplotlib #mpf會引用到matplotlib的函式故要import
import mplfinance as mpf #用來畫K線圖

def ls(): #印出當前有哪些股票的csv檔
    csvs = glob.glob("./csv/*.csv")
    print("已有的csv檔：", end=" ")
    for csv in csvs:
        print(os.path.basename(csv)[:-7], end=" ")
    print()

def view(stock_symbol: str):#四碼股票代號
    with open(f"./csv/{stock_symbol}.TW.csv") as csvfile: #打開指定檔案
        csv_reader = csv.reader(csvfile) #建立reader物件
        list_data = list(csv_reader)
        pd_data = pd.DataFrame(list_data[1:], columns=["Date","Open","High", "Low", "Close", "Adj Close", "Volume"])
        pd_data = pd_data.drop("Adj Close", axis=1) #刪除"Adj Close"行，才能符合mpf格式
        pd_data[["Open", "High", "Low", "Close", "Volume"]] = pd_data[["Open", "High", "Low", "Close", "Volume"]].astype("float64") #設定股價和成交量型別
        #pd_data[["Date"]] = pd_data[["Date"]].astype("datetime64[ns]")
        pd_data.index = pd.DatetimeIndex(pd_data["Date"])
        pd_data = pd_data.drop("Date", axis=1) 
        print(pd_data)

        mc = mpf.make_marketcolors(up='r', down='g', inherit=True) #設定顏色為漲紅跌綠
        s = mpf.make_mpf_style(base_mpf_style="yahoo", marketcolors=mc) #設定K棒形狀
        kwargs = dict(type='candle', mav=(5,20,60), volume=True, figratio=(10,8), figscale=0.75, title=stock_symbol, style=s) #把建立圖表要用的參數全放一起
        mpf.plot(pd_data, **kwargs)

if __name__ == "__main__":
    ls()
    view(input())