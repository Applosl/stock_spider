"""
stock_day Storage 保存持久化
"""
from storages.base import Storage
from datetime import datetime
from typing import List


class StockDayItemType(object):
    ts_code = ''
    trade_date = ''
    open = 0.0
    high = 0.0
    low = 0.0
    close = 0.0
    pre_close = 0.0
    change = 0.0
    pct_chg = 0.0
    vol = 0.0
    amount = 0.0
    create_at = ''

    def __init__(self, item: dict):
        self.ts_code = item.get('ts_code', '')
        self.trade_date = item.get('trade_date', '')
        self.open = item.get('open', 0.0)
        self.high = item.get('high', 0.0)
        self.low = item.get('low', 0.0)
        self.close = item.get('close', 0.0)
        self.pre_close = item.get('pre_close', 0.0)
        self.change = item.get('change', 0.0)
        self.pct_chg = item.get('pct_chg', 0.0)
        self.vol = item.get('vol', 0.0)
        self.amount = item.get('amount', 0.0)
        self.create_at = item.get('create_at', datetime.now().strftime('%Y-%m-%d, %H:%M:%S'))


class StockDay(Storage):
    """
    股票day Storage
    """

    def save(self, i: StockDayItemType):
        with self.db_connect.cursor() as cursor:
            sql = "INSERT INTO `stock_day` (`ts_code`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`, `create_at`)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            affect_num = cursor.execute(sql, (
                i.ts_code, i.trade_date, i.open, i.high, i.low, i.close, i.pre_close, i.change, i.pct_chg,
                i.vol,
                i.amount, i.create_at))
            if affect_num == 1:
                print('done')
                self.db_connect.commit()
            return True

    def save_batch(self, items: List[StockDayItemType]):
        with self.db_connect.cursor() as cursor:
            sql = "INSERT INTO `stock_day` (`ts_code`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`, `create_at`)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            tu = []
            for i in items:
                tu.append((
                    i.ts_code, i.trade_date, i.open, i.high, i.low, i.close, i.pre_close, i.change, i.pct_chg,
                    i.vol,
                    i.amount, i.create_at))
            affect_num = cursor.executemany(sql, tuple(tu))
            if affect_num == len(items):
                print('done')
                self.db_connect.commit()
            return True
