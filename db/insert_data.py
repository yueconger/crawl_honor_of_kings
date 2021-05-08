# -*- encoding: utf-8 -*-
"""
@File    : insert_data.py
@Time    : 2021/5/7 16:33
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""
import json

from db.db_mysql import MysqlDB
from conf.config import config
from utils.tools import del_none, change_html_2_wechat_tags


def _insert_data(mysqldb, sql):
    mysqldb.add(sql)


def hero_infos_table_values(values):
    dict_hero = {}
    dict_hero['rowkey'] = values.get('ename')
    dict_hero['id'] = values.get('ename')
    dict_hero['name'] = values.get('cname')
    dict_hero['title'] = values.get('title')
    dict_hero['hero_type'] = values.get('hero_type')
    dict_hero['hero_type2'] = values.get('hero_type2')
    dict_hero['new_type'] = values.get('new_type')
    dict_hero['skin_name'] = values.get('skin_name')
    hero_info = del_none(dict_hero)
    rowkey, id, name, title, hero_type, hero_type2, new_type, skin_name = hero_info['rowkey'], hero_info['id'], \
                                                                          hero_info['name'], hero_info['title'], \
                                                                          hero_info['hero_type'], hero_info[
                                                                              'hero_type2'], hero_info['new_type'], \
                                                                          hero_info['skin_name']
    insert_hero_infos_table = f"""insert into hero_infos (rowkey, id, name, title, hero_type, hero_type2, new_type, skin_name) values ({rowkey}, {id}, '{name}', '{title}', '{hero_type}', '{hero_type2}', '{new_type}', '{skin_name}')"""
    return insert_hero_infos_table


def game_equipments_values(values):
    dict_hero = {}
    dict_hero['rowkey'] = values.get('item_id')
    dict_hero['item_id'] = values.get('item_id')
    dict_hero['item_name'] = values.get('item_name')
    dict_hero['item_type'] = values.get('item_type')
    dict_hero['price'] = values.get('price')
    dict_hero['total_price'] = values.get('total_price')
    dict_hero['des1'] = values.get('des1')
    dict_hero['des2'] = values.get('des2')
    hero_info = del_none(dict_hero)
    dict_hero['des1'] = change_html_2_wechat_tags(dict_hero['des1'])
    dict_hero['des2'] = change_html_2_wechat_tags(dict_hero['des2'])
    rowkey, item_id, item_name, item_type, price, total_price, des1, des2 = hero_info['rowkey'], hero_info['item_id'], \
                                                                            hero_info['item_name'], hero_info[
                                                                                'item_type'], \
                                                                            hero_info['price'], hero_info[
                                                                                'total_price'], hero_info['des1'], \
                                                                            hero_info['des2']
    insert_hero_infos_table = f"""insert into game_equipments (rowkey, item_id, item_name, item_type, price, total_price, des1, des2) values ({rowkey}, {item_id}, '{item_name}', '{item_type}', '{price}', '{total_price}', '{des1}', '{des2}')"""
    return insert_hero_infos_table


def insert_data():
    if config.get('mysqldb').get('auto_create_tables'):
        mysqldb = MysqlDB(**config.get('mysqldb'))

        """英雄池数据库源数据"""
        # with open("../json/hero_infos.json", encoding='utf-8') as rf:
        #     result = rf.read()
        # hero_infos = json.loads(result)
        # for hero_info in hero_infos:
        #
        #     insert_hero_infos_table = hero_infos_table_values(hero_info)
        #     _insert_data(mysqldb, insert_hero_infos_table)
        #     print(insert_hero_infos_table)

        """武器装备源数据"""
        with open("../json/game_equipments.json", encoding='utf-8') as rf:
            result = rf.read()
        game_equipments = json.loads(result)
        for game_equipment in game_equipments:
            insert_game_equipments_table = game_equipments_values(game_equipment)
            _insert_data(mysqldb, insert_game_equipments_table)
            print(insert_game_equipments_table)


if __name__ == '__main__':
    insert_data()
