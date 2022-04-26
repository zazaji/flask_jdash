# -*- coding: utf-8 -*-

"""
flask_jsondash.db
~~~~~~~~~~~~~~~~~~~~~~~~~~

A translation adapter for transparent operations between storage types.

:copyright: (c) 2016 by Chris Tabor.
:license: MIT, see LICENSE for more details.
"""
import time
import json
from datetime import datetime as dt

from pymongo import MongoClient

from flask_jsondash import mongo_adapter, settings
import pandas as pd
from sqlalchemy import create_engine

DB_NAME = settings.ACTIVE_DB
DB_NAME = 'mysql'

def reformat_data(data, c_id):
    """Format/clean existing config data to be re-inserted into database.

    Args:
        data (dict): The chart data to override with standard params.

    Returns:
        data (dict): The in-place updated dict.
    """
    data.update(dict(id=c_id, date=dt.now()))
    return data


def format_charts(data):
    """Form chart POST data for JSON usage within db.

    Args:
        data (dict): The request.form data to format.

    Returns:
        modules (list): A list of json-decoded dictionaries.
    """
    modules = []
    for item in data:
        if item.startswith('module_'):
            val_json = json.loads(data[item])
            modules.append(val_json)
    return modules


class get_db_handler():

    def __init__(self):
        engine_str="mysql+pymysql://{}:{}@{}/{}?charset=utf8".format(settings.USERNAME, settings.PASSWORD, settings.DB_URI+':'+str(settings.DB_PORT), settings.DB_NAME)
        self.client = create_engine(engine_str)

    def count(self):
        conn=self.client.connect()
        sql = 'select count(*) from '+settings.DB_TABLE
        result=pd.read_sql(sql,conn).values[0]

        conn.close()
        return result
    def delete_all(self):
        conn=self.client.connect()
        sql = 'delete  from '+settings.DB_TABLE
        result=conn.execute(sql)
        conn.close()        
        return result
    def delete(self,id):
        conn=self.client.connect()
        sql = 'delete  from '+settings.DB_TABLE+" where id='"+id+"'"
        result=conn.execute(sql)
        conn.close()        
        return result
    def filter(self,clist,category):
        conn=self.client.connect()
        sql = 'select category from categories'
        result=pd.read_sql(sql,conn).values
        conn.close()
        categories=[{'category': i[0]} for i in result]
        return categories

    def create(self,data):
        conn=self.client.connect()
        # data['modules']=str(data['modules'])
        data['date']=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if('modules' in data.keys()):
            data['modules']=str(data['modules'])
        else:
            data['modules']='[]'
        result=pd.DataFrame([data]).to_sql(con=conn,name=settings.DB_TABLE,if_exists="append",index=False)
        conn.close()
        return result

    def readmodules(self,category='0',guid='0'):
        conn=self.client.connect()
        sql = 'select * from modules'
        if category!='0':
            sql+=" where category='"+str(category)+"'"
        if guid!='0': 
            sql+=" where guid='"+str(guid)+"'"
            # result=pd.read_sql(sql,conn)
        
        result=pd.read_sql(sql,conn)
        result['module']=result['module'].replace('\n','').replace('\r','')
        result['type']=result['module'].replace('\n','').replace('\r','')
        result=result.groupby('category').apply(lambda x: x.to_dict(orient='records')).to_dict()
        conn.close()
        return result

    def read(self,c_id=0):
        conn=self.client.connect()
        sql = 'select * from '+settings.DB_TABLE
        if c_id!=0:sql+=" where id='"+str(c_id)+"'"
        result=pd.read_sql(sql,conn)
        conn.close()
        result['date']=result['date'].astype('str')
        result=result.to_dict(orient='records')
        if c_id!=0:
            result=result[0]
            result['filterjson']=[
                    {'name':'year',
                    'options':[
                        {'name':'2020','value':'2020'},
                        {'name':'2021','value':'2021'}
                        ]
                    },
                    {'name':'quarter',
                    'options':[
                        {'name':'1','value':'1'},
                        {'name':'2','value':'2'},
                        {'name':'3','value':'3'},
                        {'name':'4','value':'4'}
                        ]
                    }
                ]

            result['modules']=eval(result['modules'].replace('\\',''))
            for r in result['modules']:
                conn=self.client.connect()
                module1=pd.read_sql("select * from modules where guid='{}'".format(r['guid']),conn).to_dict(orient='records')
                conn.close()
                module1=module1[0]['module']
                module1=eval(module1.replace('\n','').replace('\r',''))
                for key in module1.keys():
                    r[key]=module1[key]

                if 'refreshInterval' in r.keys():r['refreshInterval']=int(r['refreshInterval']) if r['refreshInterval'] else r['refreshInterval']
        else:
            for r in result:
                r['modules']=eval(r['modules'].replace('\\',''))
        return result


    def update(self,c_id,data,fmt_charts=False):
        conn=self.client.connect()
        modules=[]
        for module in data['modules']:
            module1={}
            if 'cachedData' in module.keys():module.pop('cachedData') 
            for item in ['type', 'family', 'dataSource', 'override', 'classes']: 
                if item in module.keys(): module1[item]=module.pop(item) 
            ismodule=conn.execute("select count(guid) from modules  where guid='"+str(module['guid'])+"'").fetchone()
            module['name']=str(module['name']).replace("\'",'').replace("\"",'')
            print(module)

            if(ismodule[0]>0):
                content=module['content'] if 'content' in module.keys() else ""

                sql = "update modules set "\
                +" name='"+ module['name'] +"',"\
                +" content='"+ content +"',"\
                +" module=\""+ str(module1)+"\""\
                +" where guid='" + str(module['guid']) + "'"
            else:
                if 'category' in data.keys():
                    pass
                else:
                    data['category']=''
                    data['content']=''
                sql = 'insert into modules(guid,name,category,module) values("{}","{}","{}","{}")'.format(
                    module['guid'],module['name'],data['category'],str(module1).replace("\"",""))

            modules.append(module)
            result=conn.execute(sql)
            # print(module)
            # print('======')
            # print(str(data['modules']))

        sql = 'update '+settings.DB_TABLE+" set "\
                +" modules=\""+ str(data['modules'])+"\","\
                +" name=\""+ str(data['name'].replace("'",''))+"\","\
                +" category=\""+ str(data['category'].replace("\"",''))+"\","\
                +" content=\""+ str(data['content'].replace("\"",''))+"\","\
                +" layout=\""+ str(data['layout'].replace("\"",''))+"\""\
                +" where id='"+data['id']+"'"

        result=conn.execute(sql)
        conn.close()
        return result


    """Get the appropriate db adapter.

    Returns:
        object: The instantiated database handler
    """

    # if DB_NAME == 'mongo':
    #     client = MongoClient(host=settings.DB_URI, port=settings.DB_PORT)
    #     conn = client[settings.DB_NAME]
    #     coll = conn[settings.DB_TABLE]
    #     return mongo_adapter.Db(client, conn, coll, format_charts)

    # if DB_NAME == 'oracle':
    #     client = MongoClient(host=settings.DB_URI, port=settings.DB_PORT)
    #     conn = client[settings.DB_NAME]
    #     coll = conn[settings.DB_TABLE]
    #     return mongo_adapter.Db(client, conn, coll, format_charts)
    # else:
    #     raise NotImplementedError(
    #         'Mongodb is the only supported database right now.')
