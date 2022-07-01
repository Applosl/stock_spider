"""
stock Storage 保存持久化
"""
from storages.base import Storage
from datetime import datetime
from typing import List


class StockItemType(object):
    ts_code = ''
    symbol = ''
    area = ''
    industry = ''
    fullname = ''
    enname = ''
    cnspell = ''
    market = ''
    exchange = ''
    curr_type = ''
    list_status = ''
    list_date = ''
    delist_date = ''
    is_hs = ''
    create_at = ''

    def __init__(self, item: dict):
        self.ts_code = item.get('ts_code', '')
        self.symbol = item.get('symbol', '')
        self.area = item.get('area', '')
        self.industry = item.get('industry', '')
        self.fullname = item.get('fullname', '')
        self.enname = item.get('enname', '')
        self.cnspell = item.get('cnspell', '')
        self.market = item.get('market', '')
        self.exchange = item.get('exchange', '')
        self.curr_type = item.get('curr_type', '')
        self.list_status = item.get('list_status', '')
        self.list_date = item.get('list_date', '')
        self.delist_date = item.get('delist_date', '')
        self.is_hs = item.get('is_hs', None)
        self.create_at = item.get('create_at', datetime.now().strftime('%Y-%m-%d, %H:%M:%S'))


class StockList(Storage):
    """
    股票列表Storage
    """

    def save(self, i: StockItemType):
        print(i.__dict__)
        with self.db_connect.cursor() as cursor:
            sql = "INSERT INTO `stock` (`ts_code`, `symbol`, `area`, `industry`, `fullname`, `enname`, `cnspell`, `market`, `exchange`, `curr_type`, `list_status`, `list_date`, `delist_date`, `is_hs`, `create_at`)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            affect_num = cursor.execute(sql, (
                i.ts_code, i.symbol, i.area, i.industry, i.fullname, i.enname, i.cnspell, i.market, i.exchange,
                i.curr_type,
                i.list_status, i.list_date, i.delist_date, i.is_hs, i.create_at))
            if affect_num == 1:
                self.db_connect.commit()
            return True

    def save_batch(self, items: List[StockItemType]):
        with self.db_connect.cursor() as cursor:
            sql = "INSERT INTO `stock` (`ts_code`, `symbol`, `area`, `industry`, `fullname`, `enname`, `cnspell`, `market`, `exchange`, `curr_type`, `list_status`, `list_date`, `delist_date`, `is_hs`, `create_at`)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            tu = []
            for i in items:
                tu.append((
                    i.ts_code, i.symbol, i.area, i.industry, i.fullname, i.enname, i.cnspell, i.market, i.exchange,
                    i.curr_type,
                    i.list_status, i.list_date, i.delist_date, i.is_hs, i.create_at))
            affect_num = cursor.executemany(sql, tuple(tu))
            if affect_num == len(items):
                self.db_connect.commit()
            return True
