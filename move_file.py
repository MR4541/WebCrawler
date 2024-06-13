#用來把stock_download.py下載的東西移到csv資料夾裡
import glob #用來搜尋檔案
import shutil #用來移動檔案
import os

def move_file(target_files, destination_dir):#要移動的目標資料夾
    files = glob.glob(target_files)
    for file in files:
        shutil.move(file, os.path.join(destination_dir, os.path.basename(file))) #把file移至destination（資料夾）
        #os.path.join可以將傳入字串自動組成路徑，如自動加/，辨識目錄順序等
        #os.path.basename可以從路徑字串中取出檔案名稱，或是最後一層的目錄名稱
        #shutil.move目標路徑若給目錄，遇到相同名稱檔案會報錯，若給指定檔案路徑則可直接覆蓋
    print(f"共{len(files)}個檔案移動完成！")
    return