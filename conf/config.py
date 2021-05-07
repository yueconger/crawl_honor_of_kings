# -*- encoding: utf-8 -*-
"""
@File    : conf.py
@Time    : 2021/4/28 1:25 下午
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""

import os
import socket
import sys
import shutil

import yaml  # pip3 install pyyaml

if 'python' in sys.executable:
    os.path.abspath(__file__)
    abs_path = lambda file: os.path.abspath(os.path.join(os.path.dirname(__file__), file))
else:
    abs_path = lambda file: os.path.abspath(os.path.join(os.path.dirname(sys.executable), file))  # mac 上打包后 __file__ 指定的是用户根路径，非当执行文件路径

config = yaml.full_load(open(abs_path('config.yaml'), encoding='utf8'))