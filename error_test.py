# import requests module
import requests
import pymysql
import pymysql.cursors

import hashlib
import sql_insert


# 資料庫參數設定
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

# Making a get request
def url_checker(url):
    try:
        #Get Url
        get = requests.get(url)
        return(get.status_code )
        #Exception
    except requests.exceptions.RequestException :
            # print URL with Errs
            wrong=0
            return(wrong)

# url='https://tailit.nccu.edu.tw/Page1Doc?fid=2104'
# print(url_checker(url))

def States_code_check():
    command = "SELECT max(E_id) FROM web_connect_error WHERE E_id >=0"
    cursor.execute(command)
    results = list(cursor.fetchone())
    E_id=int(results[0])
    return E_id

def States_code_warning(Eid):
    command = "SELECT * FROM web_connect_error WHERE E_id <=%(Eid)s"
    cursor.execute(command, { 'Eid': int(Eid) })
    results = cursor.fetchall()
    return results

# Eid=States_code_check()
# results=States_code_warning(Eid)
# for i in range(1,Eid+1):
#     print(results[i][1],results[i][2])


def html_compare(department):
    conn.commit()
    max_values=sql_insert.return_value()
    record_amount=int(max_values[1])
    time1=sql_insert.check_time(record_amount)
    record_amount=record_amount-1
    time2=sql_insert.check_time(record_amount)
    
    m = hashlib.sha256()
    Did=sql_insert.regulatory_project_check(department)
    
    command="select html from department_html where create_time=%(create_time)s and department=%(department)s"
    cursor.execute(command, { 'create_time': time1,'department' :Did})
    results1 = cursor.fetchone()
    results1 = ''.join ( ( z for z in str(results1[0]) if not z.isdigit ( ) ) )

    md5=hashlib.md5()
    md5.update(results1.encode('utf-8'))
    hash1=md5.hexdigest()

    cursor.execute(command, { 'create_time': time2,'department' :Did})
    results2 = cursor.fetchone()
    results2 = ''.join ( ( z for z in str(results2[0]) if not z.isdigit ( ) ) )
    results2=results1
    length=int(len(results2))
    # print(length)/
    results2=results2[:length]
    
    md5=hashlib.md5()
    md5.update(results2.encode('utf-8'))
    hash2=md5.hexdigest()
    # print(hash1,hash2)
    # if hash1==hash2:
    #     print('same')
    # else:
    #     print('different')
    return hash1==hash2

# 



def link_compare(department):
    max_values=sql_insert.return_value()
    record_amount=int(max_values[1])
    time1=sql_insert.check_time(record_amount)
    record_amount=record_amount-1
    time2=sql_insert.check_time(record_amount)
    Did=sql_insert.regulatory_project_check(department)
    command="select link from link_store where create_time=%(create_time)s and department=%(department)s"
    cursor.execute(command, { 'create_time': time1,'department' :Did})
    results1 = cursor.fetchall()
    # print(results1)
    cursor.execute(command, { 'create_time': time2,'department' :Did})
    results2 = cursor.fetchall()
    # print(results2)
    diff=set(results2)^set(results1)
    # print(diff)
    if diff!=set():
        return diff

    # for link1,link2 in zip(results1,results2):
    #     if link1 != link2:
    #         return link1,link2
            
def error_report_insert(deppartment,error_time,error_type,error_describe):
    command = "INSERT INTO error_report(deppartment,error_time,error_type,error_describe)VALUES(%s,%s, %s, %s)"
    cursor.execute(command,(deppartment,'2023-05-22 02:37:36',error_type,error_describe))

# Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# error_report_insert('歷史系','2023-05-22 02:37:36','Status code error','404')

# command = "INSERT INTO error_report(deppartment,error_time,error_type,error_describe)VALUES('歷史系','2023-05-22 02:37:36','Status code error','404')"
# cursor.execute(command)


def url_report_check(R_url):
    command="select Did from regulatory_web where R_url=%(R_url)s"
    cursor.execute(command, { 'R_url': R_url})
    result = cursor.fetchone()
    if result==None:
        return('false1')
    command="select * from error_report where Did=%(Did)s"
    cursor.execute(command, { 'Did': result})
    result = cursor.fetchone()
    conn.commit()
    if result==None:
        return False
    return True
# ans=url_report_check("https://thinker.nccu.edu.tw/")
# print(ans)

def error_report_return(R_url):
    command="select Did from regulatory_web where R_url=%(R_url)s"
    cursor.execute(command, { 'R_url': R_url})
    result = cursor.fetchone()
    command="select * from error_report where Did=%(Did)s"
    cursor.execute(command, { 'Did': result})
    results = cursor.fetchall()
    # print(len(result))
    new_result=[]
    for result in results:
        result=list(result)
        result[0]=R_url
        new_result.append(result)
    return new_result
# print(error_report_return("https://history.nccu.edu.tw/"))


def photo_hash_return(department,time):
    conn.commit()
    command="select photo_hash from department_html where department=%(department)s and create_time = %(time)s"
    cursor.execute(command, { 'department': department,'time':time})
    result = cursor.fetchone()
    if result==None:
        return None
    return result[0]

# print(photo_hash_return('3','2023-08-08 16:05:28'))

# link_compare('哲學系')
# sql_insert.sql_commit()   
conn.commit()