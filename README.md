
# Website-Change-Detection-System
在網站輸入欲查詢變動之網頁，系統會呈現網頁更動或如未有詢問是否登記持續追蹤並由後台系統隔一段時間比對差異。

## Prerequisites

- python
- Webdriver
- selenium
- Flask
- MySQL
- beautifulsoup4
- Request
- cv2

# Webdriver 
* 功能:WebDriver操作瀏覽器的一個介面，使用程式可以自動化操控WebDriver來進行登入帳號、自動輸入或是捲動頁面等，來達成靜態爬蟲無法做到的功能
* 先到 http://chromedriver.chromium.org/downloads 下載符合版本的ChromeDriver
* ChromeDriver不一定即時更新，如果未有版本，至https://googlechromelabs.github.io/chrome-for-testing/ 下載符合版本的ChromeDriver
* 選擇 chromedriver_win32.zip，下載完成後，解壓縮後，就會看到 chromedriver.exe
* 將chromedriver.exe放到跟python.exe一樣的目錄下(也可放在和欲執行程式相同檔案夾)

# selenium
* 功能:透過 selenium 可以模擬出使用者在瀏覽器的所有操作行為，實作中主要用於網頁原始碼的抓取以及原始碼內tag內容的提取
* 安裝套件 `pip install selenium`
* 啟動 `web_html_downlod.py`開啟後台系統定期追蹤


# Flask
* 功能:使用Python編寫的輕量級Web應用框架，實作中主要用於網頁編寫
* 安裝套件 `pip install Flask`
* 啟動 `website.py`開啟登記網頁運行
* http://localhost:5000/

#  MySQL
* 功能:資料庫管理系統，需要在程式碼安裝套件使用，實作中主要用於儲存爬蟲下來的資料及比對結果。
* 安裝套件 `pip install pymysql'
* Mysql檔檔案夾內檔案載入自己資料夾內
* 所有出現db_setting的python檔內，改為自己MySQL的帳號密碼

#  beautifulsoup4 
* 功能:解析網頁架構，取得想要的局部資料，實作中主要用於網頁原始碼的抓取以及原始碼內tag內容的提取
* 安裝套件 `pip install beautifulsoup4'


# Request
* 功能:透過 requests 可以對 HTTP 發送請求，抓取網頁的資料，實作中主要用於Http Status Code的獲取
* 安裝套件 `pip install requests'

# cv2
* 功能:一個跨平台的電腦視覺套件，實作中主要用於照片的獲取比對
* 安裝套件 `pip install numpy'
* 安裝套件 `pip install matplotlib'
* 安裝套件 `pip install opencv-python'
