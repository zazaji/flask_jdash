from flask import Flask

import os
from flask import render_template, flash, redirect, url_for, current_app, \
    send_from_directory, request, abort, Blueprint,jsonify
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import func
from sqlalchemy import create_engine

import numpy as np
import pandas as pd
import time
import json
##########################################################

app = Blueprint('service_blueprint',__name__)
# rownum=1000
ip='10.10.163.151:3306'
dbname='201'
user='root'
password='123456'
engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset=utf8".format(user, password, ip, dbname))
# sql='select * from i_sjkwhb2 sqls left join i_sjkwhb1 dbs on (sqls.ip=dbs.ip and sqls.slm=dbs.slm )'
# # sql='select * from i_sjkwhb1'
# conn=engine.connect()
# data=pd.read_sql(sql,conn)
# data=data[['l', 'mc', 'cs', 'stmc','fhz',
#             'lx','ip','dk','slm','yhm1', 
#             'mm', 's','gxzq']].T.drop_duplicates().T.set_index('cs')
# ##'列','名称','请求参数','视图名称','返回值','ip','端口','实例名','用户名','密码','sql语句','更新周期'
# conn.close()

##################################################
import re
def trans_sql(y):
    y= y.replace('<br />','\n').replace('&nbsp;',' ').replace('\\n','\n').replace('&gt;','>').replace('&lt;','<')[24:-1]
    return re.sub(' +',' ',y)



# 从数据库中调取请求和数据库试图的对应关系
def reqest_data(req,parameter):
    validated=0
    if parameter['user']=='user' and parameter['pass']=='user':
        validated=1

    if validated==1:
        sql="select * from i_sjkwhb2 sqls left join i_sjkwhb1 dbs on (sqls.ip=dbs.ip and sqls.slm=dbs.slm )"
        if req!="": sql+=" where sqls.cs='{}'".format(req)
        conn=engine.connect()
        data=pd.read_sql(sql,conn)
        data=data[['l', 'mc', 'cs', 'stmc','fhz','lx','ip','dk','slm','yhm1', 'mm', 's','gxzq']]
        ##'列','名称','请求参数','视图名称','返回值','ip','端口','实例名','用户名','密码','sql语句','更新周期'
        conn.close()
        data['s']=data['s'].astype('str')
        data['s']=[ trans_sql(y) for y in data['s'].values]
        if req=="":
            return list(data.to_dict(orient='index').values())
        if len(data)>0:
            return list(data.to_dict(orient='index')[0].values())

    return []   

def get_sql(dbtype,ip,port,dbname,user,password,sql):
    if 'oracle' in dbtype:
        engine1 = create_engine('oracle://{}:{}@{}:{}/?service_name={}'.format(user, password, ip,port, dbname))
        # sql=sql+' where rownum<' + str(rownum)

    elif 'mysql' in dbtype: 
        engine1 = create_engine("mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(user, password, ip,port,dbname))
        sql=sql+' limit 100'
    conn=engine1.connect()
    data=pd.read_sql(sql,conn).fillna('')
    conn.close()
    return data

def format_json(data,parameter):
    if parameter['t'] in ['index']:
        data=data.to_dict(orient=parameter['t'])
    else :
        data=data.to_dict(orient='index')
    return data

#####################################################
@app.route('/')
def index():
    return 'this is API Home'

@app.route('/listapi')
def listapi():
    parameter=dict(request.args)
    result=reqest_data('',parameter)
    return result


@app.route('/api/<r>/',methods=['GET'])
def api(r):
    parameter=dict(request.args)
    # 获取请求数据库关系,request.args
    req_data=reqest_data(r,parameter)
    column,dname,req,viewname,resp,dbtype,ip,port,dbname,\
        username,password,sqls,period=req_data
    #'l', 'mc', 'cs', 'stmc','fhz','lx','ip','dk','slm','yhm1', 'mm', 's','gxzq'
    data=get_sql(dbtype,ip,port,dbname,user,password,sqls)
    data=format_json(data,parameter)
    return data 
###############################################
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=84,debug=True)





