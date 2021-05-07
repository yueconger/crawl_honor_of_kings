# -*- encoding: utf-8 -*-
"""
@File    : create_db.py
@Time    : 2021/4/28 1:24 下午
@Author  : yuecong
@Email   : yueconger@163.com
@Software: PyCharm
"""

from db.db_mysql import MysqlDB
from conf.config import config


def _create_table(mysqldb, sql):
    mysqldb.execute(sql)


def create_table():
    hero_infos_table = '''
    CREATE TABLE IF NOT EXISTS `hero_infos` (
        `rowkey` int NOT NULL COMMENT '主键',
        `id` int NOT NULL,
        `name` varchar(50) DEFAULT NULL COMMENT '英雄名称',
        `title` varchar(200) NOT NULL COMMENT '英雄标题',
        `hero_type` varchar(50) COMMENT '英雄默认定位',
        `hero_type2` varchar(50) COMMENT '英雄第二定位',
        `new_type` varchar(50) COMMENT '英雄新定位',
        `skin_name` longtext COMMENT '纯文本详情',
        `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
        `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
        PRIMARY KEY (`rowkey`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='英雄展示表'
    '''

    game_equipments_table = '''
        CREATE TABLE IF NOT EXISTS `game_equipments` (
            `rowkey` int NOT NULL COMMENT '主键',
            `item_id` int NOT NULL,
            `item_name` varchar(50) DEFAULT NULL COMMENT '装备名称',
            `item_type` varchar(50) NOT NULL COMMENT '装备类型',
            `price` varchar(50) COMMENT 'price',
            `total_price` varchar(50) COMMENT '装备价格',
            `des1` longtext COMMENT '装备描述1',
            `des2` longtext COMMENT '装备描述2',
            `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
            `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
            PRIMARY KEY (`rowkey`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='游戏装备表'
        '''

    if config.get('mysqldb').get('auto_create_tables'):
        mysqldb = MysqlDB(**config.get('mysqldb'))
        _create_table(mysqldb, hero_infos_table)
        _create_table(mysqldb, game_equipments_table)


if __name__ == '__main__':
    create_table()
