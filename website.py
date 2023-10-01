from flask import Flask,render_template
from flask import url_for,redirect
from flask import Flask,render_template, make_response
import json
import sql_insert
import error_test
from flask import request

import pymysql
import pymysql.cursors
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

app = Flask(__name__, '/static')
app.config["JSON_AS_ASCII"] = False

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == "POST"):
        if request.values.get("check_all")=='查看當前已登記網站列表':
            return redirect(url_for('list_all'))

        check_url=request.form["url"]
        conn.commit()
        check=error_test.url_report_check(request.form["url"])
        # print(check)
        if(check==True):
            
            response =make_response(redirect(url_for('report')))
            # response.set_cookie('url',check_url )
            response.set_cookie('url',json.dumps(check_url))
            return response
        if(check==False):
            check=str(check)
            return render_template('main.html',check_url=check)
        check=str(check)
        if(check=='false1'):
            response =make_response(redirect(url_for('insert'))) 
            response.set_cookie('url',check_url )
            return response
    # if request.values['yes/no']=='是':
    
    #     return render_template('main.html',check_url='true1')
    # if request.values['yes/no']=='否':
    #     render_template('main.html',name="")
    if(request.method == "GET"):
        return  render_template('main.html',name="")

# @app.route('/report2', methods=['GET', 'POST']) 
# def report2():
#     return render_template('report.html')

@app.route('/report', methods=['GET', 'POST']) 
def report():
    url = request.cookies.get('url')
    url=json.loads(url)
    # print(url)
    # messages=sql_insert.regulatory_web_inf()
    amount=0
    urls=[]
    err_informs=[]
    if type(url)==str:
        urls.append(url)
    else:
        urls=url
    # print(urls)
    normal_web=[]
    for url in urls:
        url_amount=sql_insert.error_amount(url)
        amount+=url_amount
        # print(url_amount)
        if url_amount==0:
            normal_web.append(url)
        else:
            err_informs+=error_test.error_report_return(url)
    # urls.append(url)
    # print(err_informs)
    if normal_web==[]:
        normal_web="False"
    # print(err_informs)
    # normal_web=normal_web
    return render_template('New_report.html',messages=urls,url_links=urls,change_amount=amount,err_informs=err_informs,normal_web=normal_web)

@app.route('/insert/', methods=['POST', 'GET']) 
def insert():
    # global url
    url=[]
    url = request.cookies.get('url')
    print(url)
    if(request.method == "GET"):
        return render_template('new.html',url=url)
    if(request.method == "POST"):
        # bt_y=request.values.get("yes")
        # bt_n=request.values.get("no")	
        # print(bt_y,bt_n)
        if request.values.get("yes")=='yes':
      
            # print(url)
            sql_insert.regulatory_web_insert(str(url))
            conn.commit()
            return redirect(url_for('index'))
        if request.values.get("no")=='no':
            # print('no')
            return redirect(url_for('index'))
    return render_template('new.html',url=url)

@app.route('/list_all', methods=['GET', 'POST']) 
def list_all():
    web_list=sql_insert.list_web()
    if (request.method == "POST"):
        urls=request.form.getlist('web_url')
        response =make_response(redirect(url_for('report')))
        response.set_cookie('url',json.dumps(urls))
        return response
    return render_template('check_web_list.html',web_list=web_list)
    

if __name__ == '__main__':
	app.run(host='0.0.0.0',port='5000',debug=True)