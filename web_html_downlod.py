from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import imagehash
import requests
from bs4 import BeautifulSoup as Soup
import time
import ssl
import certifi
from urllib.request import urlopen
import re
import time
import requests
import urllib.request
import hashlib
from sql_insert import return_value,chronology_insert,link_insert,UPDATE_value
import sql_insert
import datetime
import error_test
import web_check
import cv2

# def storelink(links,name):
#     link_f = open(name, 'w', encoding='UTF-8')
#     for l in links:
#         print(l,file=link_f)
#     f.close()

def replace_all_blank(value):
    result = re.sub('\W+', '', value).replace("_", '')
    # print(result)
    return result

request = "https://example.com"
urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))


options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
 
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.maximize_window()

# chrome= requests.get(driver.current_url)
# soup = Soup(chrome.text,'html5lib')
# tags=soup.find_all('a',target="_blank")



values=return_value()
record_aomount=values[1]
link_amount=values[2]
# print(record_aomount,link_amount)
# while True:
# while True:
i=0
while i in  range(3):
    record_aomount+=1
    
    # print(record_aomount)
    # driver.get("https://www.nccu.edu.tw/p/426-1000-55.php?Lang=zh-tw")
    # time.sleep(3)
    localtime = time.localtime()
    Now = str(time.strftime("%Y-%m-%d-%I%M%S", localtime))
    #store name
    now_time= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chronology_insert(record_aomount,now_time)
    
    departments=sql_insert.list_web()
    # print(departments)
    
    Status_codes=[]
    departments2=[]
    for department in departments:
        url2=department[0]
        departments2.append(url2)
        # print(url2)
        response = error_test.url_checker(url2)
        Status_codes.append(response)
    # print('Status_codes:')
    # print(Status_codes)
    # Status_codes2=Status_codes
    # print(len(Status_codes),len(departments))
    #check each department
    for (department,status) in zip(departments2,Status_codes):
        name=department
        print(name)
        # Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if status>=200 and status<=399 :
            driver.get(department)
            time.sleep(3)
            # driver.get_screenshot_as_file("screenshot.png")
            photo_addr=driver.find_element(By.TAG_NAME,"img").get_attribute('src')
            urllib.request.urlretrieve(photo_addr,"photo.png")
            img=cv2.imread("photo.png")
            hash1=web_check.aHash(img)
            time.sleep(7)
            html1= driver.page_source
            soup = Soup(html1,'html5lib')
            html1=str(html1)
            
            # print(hash1)

            sql_insert.sql_data_insert(department,now_time,html1,hash1)
            
            

            #used_url_insert
            link=[]
            type=[]
            
            links=driver.find_elements(By.XPATH,'//*[@href]')
            for l in links:
                ll=l.get_attribute('href')
                if ll :
                    link.append(ll)
                    type.append('href')
            links2=driver.find_elements(By.XPATH,'//*[@src]')
            # link.append('ll')
            for l in links2:
                # print(l.text)
                ll=l.get_attribute('src')
                if ll != None:
                    link.append(ll)
                    type.append('src')

            titles=driver.find_elements(By.XPATH,'//*[@title]')
            for t in titles:
                title=t.get_attribute('title')
                if title != None:
                    link.append(title)
                    type.append('title')


            alts=driver.find_elements(By.XPATH,'//*[@alt]')
            for t in alts:
                alt=t.get_attribute('alt')
                if alt != None:
                    link.append(alt)
                    type.append('title')

            chrome= requests.get(driver.current_url)
            soup = Soup(chrome.text,'html5lib')
            for p in soup.find_all('p'):
                link.append(p.get_text())
                type.append('p')

            # p2=driver.find_elements(By.TAG_NAME,'p')
            # for p in p2:
            #     if not replace_all_blank(p.text) :               
            #         link.append( replace_all_blank(p.text))
            #         type.append('p')
            # # print(p[1])

            # link_file='old2/'+'link_'+name+Now+'.txt'
            # storelink(link,link_file)

            for (ll,ty) in zip(link,type):
                link_amount+=1
                link_insert(link_amount,name,now_time,ll,ty)
            # driver.close()
            time.sleep(2)
            sql_insert.sql_commit()
        else:
            # print("Status code waring")
            sql_insert.HTTP_Status_warning(name,now_time,status)
            html1= driver.page_source
            soup = Soup(html1,'html5lib')
            html1=str(html1)


        UPDATE_value(record_aomount,link_amount)
        sql_insert.sql_commit()
    # break

    # sql_insert.sql_commit()
    # print(Status_codes2)
    for (department,status) in zip(departments2,Status_codes):
        # print(department,status)
        # print('test1')
        status=int(status)
        # print(status,department)
        
        if status>399 or status<200:
            sql_insert.error_report_insert(department,now_time,'Status_codes_error',status)
        else:
            max_values=sql_insert.return_value()
            record_amount=int(max_values[1])-1
            # print(record_amount)
            if record_amount>0:
                time1=sql_insert.check_time(record_amount)
                Did=sql_insert.regulatory_project_check(department)
                record_amount=record_amount+1
                hash1=error_test.photo_hash_return(Did,time1)
                
                if hash1!=None:
                    time2=sql_insert.check_time(record_amount)
                    hash2=error_test.photo_hash_return(Did,time2)
                    if hash1!=hash2:
                        # print(hash1,hash2)
                        sql_insert.error_report_insert(department,now_time,'photo_change','網頁第一張照片更改了')

                    link_error=error_test.link_compare(department)
                    # print(link_error)
                    
                    if link_error != None:
                        # link=str(link_error[0][0])+' and ' + str(link_error[1][0])
                        sql_insert.error_report_insert(department,now_time,'url_different',link_error)
                    html_error=error_test.html_compare(department)
                    # print('test3')
                    if link_error == False:
                        sql_insert.error_report_insert(department,now_time,'url_different',"html_hash_deffer")
                    # print(1)
    time.sleep(300)

# import web_comparison

# # for department in departments:
# #     name=re.sub('[^\u4e00-\u9fa5]+','',department)
# #     file1='old2/'+name+'-'+Time[0]+'.txt'
# #     file2='old2/'+name+'-'+Time[1]+'.txt'
# #     web_comparison.filecompare(file1,file2,department)
    

# time_f.close()
# sql_insert.sql_commit()

# print(departments)

driver.close()


