"""
stock_list_task
每天股票抓取任务
"""
import os
import requests
from typing import List
from tasks.task import Task
from storages.stock_day import StockDay, StockDayItemType


def _to_stock_dict(item, fields):
    if len(fields) != len(item):
        return None
    di = {}
    for k, i in enumerate(fields):
        di[fields[k]] = item[k]
    return di


class StockDailyTask(Task):
    _name = 'day_stock'
    _token = os.getenv("TUSHARE_TOKEN", "")

    def run(self):
        day = self._args.get('day', '')
        if not day:
            print('缺失必要参数day')
            return
        offset = 0
        limit = 5000

        items = []
        fields = []
        while True:
            data = self.fetch_data_pack(ts_code, limit, offset)
            if data is False:
                print('接口错误')
                return
            if len(data['items']) <= 0:
                break
            items += data['items']
            fields = data['fields']
            offset += limit

        item_type_set = self._build_item(items, fields)
        self._save_db(item_type_set)

    def fetch_data_pack(self, day: str, limit: int, offset: int):
        session = requests.session()
        data = {
            'api_name': 'daily',
            'token': self._token,
            'params': {
                "ts_code": ts_code,
                "limit": limit,
                "offset": offset

            },
            'fields': 'ts_code,trade_date,open,high,low,close,pre_close,change,pct_chg,vol,amount',
        }
        resp = session.post(url='http://api.tushare.pro', json=data, timeout=10)
        resp_data = resp.json()
        session.close()

        if resp_data['code'] != 0:
            return False
        return resp_data['data']

    def _build_item(self, items, fields):
        item_type_set = []
        for i in items:
            # 转换成dict
            di = _to_stock_dict(i, fields)
            if di is None:
                continue
            item_type_set.append(StockDayItemType(di))
        return item_type_set

    def _save_db(self, item_type_set: List[StockDayItemType]):
        store = StockDay()
        store.save_batch(item_type_set)
