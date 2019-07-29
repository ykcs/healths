# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:08:53 2019

@author: Administrator
"""

from flask import Flask
from flask import render_template
from flask import request
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

    
app = Flask(__name__)


# 生成路由关系，并把关系保存到某个地方,app对象的 url_map字段中
@app.route('/jkgl')  # @decorator
def index():
    
    return render_template('jkgl.html')

@app.route('/jk')  # @decorator
def healog():
    
    return render_template('healog.html')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5050)
    
    
