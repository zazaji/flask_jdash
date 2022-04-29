# Flask_jdash   [中文](readme_cn.md)
## Introduction
This Project isbased on [Flask_jsondash](https://github.com/christabor/flask_jsondash), and  I did some interesting to achieve the following:

1. mongodb to mysql.
2. Dynamic data refresh support.
3. ready-made charts can be directly referenced to the current dashboard.
4. Support data linkage
5. Add echarts Support
6. Add 3d-force-graph Support
7. 
## Informations
1. app.py main entry point.
2. api.py : example api .
3. serviceapi.py : You can Convert the database to a JSON interface.


## How to use
1. Clone from git,
2. Install from requirements.txt, 
3. Import sample.sql to your database , the sql is just same examples ,you can modify the database .
4. Add your mysql username and password to flask_jsondash/settings.py ,
5. Make sure port 8080 was not occupied,  and then run python app.py ,
6. Open your web browser and enjoy it.

## Something important
1. This project is based on d3.js v3, and not supported  d3js v4 and above.


Thanks:
https://github.com/christabor/flask_jsondash