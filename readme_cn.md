# Flask_jdash   [English](readme.md)



## Introduction
在Flask_jsondash的基础上，做了深度改造，实现以下内容：

1. 支持mysql。
2. 支持数据动态刷新。
3. 模块化引用，做好的图表可以直接引用到当前仪表板。
4. 支持数据联动。
5. 增加echart支持。
6. 增加3d-force-graph支持。
7. 

## 文件介绍
1. app.py 主程序，通过python运行
2. api.py : 示例api，大部分来源于flask_jsondash
3. serviceapi.py : 可以将数据库表转换为json接口api




## 使用方法
1. Clone from git.
2. 安装依赖通过 requirements.txt
3. 修改用户名、密码 flask_jsondash/settings.py 
4. 导入sample.sql数据导数据库,这仅仅是测试数据，你可以自由更改
5. 确认8080端口未被占用，如果有冲突请修改app.py
6. 设置并运行 python app.py 
7. 打开浏览器，进入127.0.0.1:8080

## 其他事项
1. 前端js基于d3.js v3，不支持v4及以上版本。


参考:
https://github.com/christabor/flask_jsondash