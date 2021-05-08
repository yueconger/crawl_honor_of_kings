# -*- encoding: utf-8 -*-
"""
@File    : tools.py
@Time    : 2021/5/7 17:14
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""
import re


def del_none(item):
    """
    字典中key-value去除空值
    :param item:
    :return:
    """
    for k, v in dict(item).items():
        if v:
            pass
        elif v == 'null' or v == 'None':
            item[k] = ""
        else:
            item[k] = ""
    return item


def change_html_2_wechat_tags(values):
    result = ''
    if values:
        values = re.sub('<div>', '<view>', values)
        values = re.sub('</div>', '</view>', values)
        values = re.sub('<p>|<span>|<h\d+>', '<text>', values)
        values = re.sub('</p>|</span>|</h\d+>', '</text>', values)
        values = re.sub('<br>', '\n', values)
        result = values
    return result
