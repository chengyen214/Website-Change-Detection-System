import pymysql
import pymysql.cursors
import datetime
import time
import web_check
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
# �????庫�????�設�?

db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "資料庫管理員密碼",
    "db": "html_check",
    "charset": "utf8", 
    "autocommit" : 1
}
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()

def regulatory_project_check(R_url):
    command = "SELECT Did FROM regulatory_web WHERE R_url = %(R_url)s"
    cursor.execute(command, { 'R_url': R_url })
    Did=cursor.fetchone()
    if(Did== None):
    
        return False
    else:
        return Did[0]

# regulatory_project_check('中�?????學系')


def sql_data_insert(department,Now,html,photo_hash):
    Did=regulatory_project_check(department)
    command = "INSERT INTO department_html(department, create_time,html,photo_hash)VALUES(%s, %s,%s,%s)"
    cursor.execute(command,(int(Did),Now,html,photo_hash))
    conn.commit()
    
def sql_commit():
    conn.commit()

# def sql_link_insert(department,Now,html,photo_hash):
#     command = "INSERT INTO department_html(department, create_time,html,photo_hash)VALUES(%s, %s,%s,%s)"

def return_value():
    command = "SELECT * FROM max_value WHERE Mid = 1"
    cursor.execute(command)
    results = cursor.fetchall()
    # for result in results: 
    #     value=list(result)
    value=list(results[0])
    return value

def chronology_insert(Tid,creat_time):
    print(Tid,creat_time)
    command = "INSERT INTO chronology(Tid, create_time)VALUES(%s, %s)"
    cursor.execute(command,(int(Tid),creat_time))
    conn.commit()




def link_insert(lid,department,Now,link,type):
    Did=regulatory_project_check(department)
    command = "INSERT INTO link_store(Lid,department,create_time,link,type)VALUES(%s, %s, %s, %s,%s)"
    cursor.execute(command,(int(lid),int(Did),Now,link,type))
    conn.commit()

# lid=1
# department='中�?????學系'
# Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# link='https://chinese.nccu.edu.tw/assets/css/page.css'
# link_insert(lid,department,Now,link)
# print('success')

def UPDATE_value(record_aomount,link_amount):
    command = "UPDATE max_value SET record_amount = %s,link_amount=%s WHERE Mid = 1"
    cursor.execute(command,(int(record_aomount),int(link_amount)))

def HTTP_Status_warning(department,now,status):
    command = "SELECT max(E_id) FROM web_connect_error WHERE E_id >=0"
    cursor.execute(command)
    results = list(cursor.fetchone())
    # print(results)
    # print(results)
    if results[0]==None:
        E_id=1
    else:
        E_id=int(results[0])
        E_id=E_id+1
    # for result in results:
    #     E_id=list(result)
    Did=regulatory_project_check(department)
    command = "INSERT INTO web_connect_error(E_id,web_err_depart,web_err_time,Web_Status_codes)VALUES(%s,%s, %s, %s)"
    cursor.execute(command,(int(E_id),int(Did),now,int(status)))
    conn.commit()

# Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# code=int(404)
# HTTP_Status_warning('??�學�?',Now,code)

# UPDATE_value(1,1)

# Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# chronology_insert(1,Now)
# print(1)

def html_hash_compare():

    command = "SELECT * FROM max_value WHERE Mid = 1"
    cursor.execute(command)
    results = cursor.fetchall()
    for result in results: 
        value=list(result)
    command2 = "SELECT * FROM chronology WHERE Mid = (Tid)VALUES(%s)"
    cursor.execute(command2(value[1]))
    cursor.fetchall()
# values=return_value()
# print(values[0],values[1],values[2])

# Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# sql_data_insert('中�?????學系',Now)
# sql_commit()

def check_time(Tid):
    command = "SELECT create_time FROM chronology WHERE Tid =%(Tid)s"
    cursor.execute(command, { 'Tid': int(Tid) })
    values=cursor.fetchone()
    sql_commit()
    # print(values)
    values=values[0]
    return str(values)

def regulatory_web_insert(url):
    command = "SELECT max(Did) FROM regulatory_web Where  Did>=0"
    cursor.execute(command)
    Did=cursor.fetchone()
    New_id=int(Did[0]+1)
    command = "INSERT INTO regulatory_web(Did,R_url)VALUES(%s, %s)"
    cursor.execute(command,(New_id,url))
    conn.commit()
    return New_id
def regulatory_web_inf():
    command = "SELECT R_url FROM regulatory_web Where  Did>=0"
    cursor.execute(command)
    values=cursor.fetchall()
    return values
# regulatory_web_insert("https://i.nccu.edu.tw/Login.aspx?ReturnUrl=%2fHome.aspx")
# print(regulatory_web_inf())

def error_amount(url):
    Did=regulatory_project_check(url)
    command = "SELECT count(*) FROM error_report Where  Did=%(Did)s"
    cursor.execute(command, { 'Did': int(Did) })
    values=cursor.fetchone()
    sql_commit()
    values=values[0]
    return values

def list_web():
    command = "SELECT R_url FROM regulatory_web "
    cursor.execute(command)
    values=cursor.fetchall()
    return values

def error_report_insert(department,time,error_type,error_describe):
    Did=regulatory_project_check(department)
    command = "INSERT INTO error_report(Did,error_time,error_type,error_describe)VALUES(%s, %s, %s, %s)"
    cursor.execute(command,(int(Did),time,error_type,str(error_describe)))
    conn.commit()
# print(list_web())
# error_report_insert('https://history.nccu.edu.tw/','2023-08-08 16:20:52','Status code error','404')
    
# print(error_amount("https://history.nccu.edu.tw/"))
# values=check_time(2)
# print(values)

conn.commit()
