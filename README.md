
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
* 先到 http://chromedriver.chromium.org/downloads 下載符合版本的ChromeDriver
* ChromeDriver不一定即時更新，如果未有版本，至https://googlechromelabs.github.io/chrome-for-testing/ 下載符合版本的ChromeDriver
* 選擇 chromedriver_win32.zip，下載完成後，解壓縮後，就會看到 chromedriver.exe
* 將chromedriver.exe放到跟python.exe一樣的目錄下(也可放在和欲執行程式相同檔案夾)

# selenium
* 安裝套件 `pip install selenium`
* 啟動 `web_html_downlod.py`開啟後台系統定期追蹤


# Flask
* 安裝套件 `pip install Flask`
* 啟動 `website.py`開啟登記網頁運行
* http://localhost:5000/

#  MySQL
* 安裝套件 `pip install pymysql'
* Mysql檔檔案夾內檔案載入自己資料夾內
* 所有出現db_setting的python檔內，改為自己MySQL的帳號密碼

#  beautifulsoup4
* 安裝套件 `pip install beautifulsoup4'


# Request
* 安裝套件 `pip install requests'

# cv2
* 安裝套件 `pip install numpy'
* 安裝套件 `pip install matplotlib'
* 安裝套件 `pip install opencv-python'
