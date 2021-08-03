"""
 -*- coding: utf-8 -*-
 @File  : inputfile.py
 @Author: yanjie
 @Date  : 2021/8/2 0002
 @功能描述  :用python接收html页面上传的文件
 @实现步骤：
    1.
    2.
    3.
"""

import os
from bottle import *

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>定义input type="file" 的样式</title>
<style type="text/css">
body{
font-size:14px;
align-text:center;
}
input{ 
vertical-align:middle;
margin:0;
padding:0
}
.file-box{
position:relative;
width:340px;
margin:0px auto;
}
.txt{
height:22px;
border:1px solid #cdcdcd;
width:180px;
}
.btn{
background-color:#FFF;
border:1px solid #CDCDCD;
height:24px;
width:70px;
}
.file{
position:absolute;
top:0;
right:80px;
height:24px;
filter:alpha(opacity:0);
opacity: 0;
width:260px
}
</style>
</head>
<body>
<div class="file-box">
<form action="/upload" method="post" enctype="multipart/form-data">
<input type='text' name='textfield' id='textfield' class='txt' />  
<input type='button' class='btn' value='浏览...' />
<input type="file" name="fileField" class="file" id="fileField" size="28" onchange="document.getElementById('textfield').value=this.value" />
<input type="submit" name="submit" class="btn" value="上传" onclick=""/>
</form>
</div>
</body>
</html>
"""

base_path = os.path.dirname(os.path.realpath(__file__))  # 获取脚本路径

upload_path = os.path.join(base_path, 'upload')  # 上传文件目录
if not os.path.exists(upload_path):
    os.makedirs(upload_path)


@route('/', method='GET')
@route('/upload', method='GET')
@route('/index.html', method='GET')
@route('/upload.html', method='GET')
def index():
    """显示上传页"""
    return HTML


@route('/upload', method='POST')
def do_upload():
    """处理上传文件"""
    filedata = request.files.get('fileField')

    if filedata.file:
        file_name = os.path.join(upload_path, filedata.filename)
        try:
            filedata.save(file_name)  # 上传文件写入
        except IOError:
            return '上传文件失败'
        return '上传文件成功, 文件名: {}'.format(file_name)
    else:
        return '上传文件失败'


@route('/favicon.ico', method='GET')
def server_static():
    """处理网站图标文件, 找个图标文件放在脚本目录里"""
    return static_file('favicon.ico', root=base_path)


@error(404)
def error404(error):
    """处理错误信息"""
    return '404 发生页面错误, 未找到内容'


run(port=8080, reloader=False)  # reloader设置为True可以在更新代码时自动重载
